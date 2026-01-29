Minimal Example
===============

Walk through the ``examples/gym_interface_demo.ipynb`` notebook with a step-by-step setup. This example demonstrates a simple LLM-driven humanoid that navigates using direct movement commands.

Prerequisites
-------------

- Install the Python client and have the UE backend running (see :doc:`installation`).
- Ensure the backend is reachable (default ports 9000). If you changed ports, pass them through command line arguments ``--cvport 9001`` or change the ``/SimWorld/Binaries/Win64/unrealcv.ini``.
- Set an OpenAI-compatible API key in your environment (the demo uses ``gpt-4o`` for the agent).

.. code-block:: bash

   export OPENAI_API_KEY="<your_api_key>"

.. note::

   You can swap models or providers by changing ``BaseLLM`` parameters. See :doc:`../components/agent_system` for interfaces.

1. Import and configure
-----------------------

.. code-block:: python

   import sys
   import os
   import time
   import re
   import math
   from pathlib import Path

   sys.path.append(str(Path().resolve().parent))  # make repo importable

   from simworld.config import Config
   from simworld.communicator.communicator import Communicator
   from simworld.communicator.unrealcv import UnrealCV
   from simworld.llm.base_llm import BaseLLM
   from simworld.map.map import Map
   from simworld.agent.humanoid import Humanoid
   from simworld.utils.vector import Vector

Create the communicator to talk to the UE backend:

.. code-block:: python

   communicator = Communicator(UnrealCV())

Set your OpenAI API key:

.. code-block:: python

   import os
   os.environ['OPENAI_API_KEY'] = '<your_openai_api_key>'

2. Define an LLM agent for navigation
--------------------------------------

The agent uses an LLM to decide actions based on its current position, direction, and target location:

.. code-block:: python

   class Agent():
       def __init__(self):
           self.llm = BaseLLM("gpt-4o")
           self.system_prompt = """You are an intelligent agent in a 3D simulation world.
   Your task is to navigate to the target position by choosing appropriate actions. Do not keep rotating in circles.

   You can only output ONE of the following actions:
   - "forward <duration>": Move forward for <duration> seconds (e.g., "forward 2")
   - "rotate <angle> <direction>": Rotate <angle> degrees in <direction> (left/right) (e.g., "rotate 45 left")
   - "wait": Do nothing for 1 seconds

   Output ONLY the action command, nothing else."""

       def action(self, obs, target):
           """Decide next action based on observation and target position.
           
           Args:
               obs: Dictionary containing:
                   - 'position' (Vector): Current 2D position
                   - 'direction' (Vector): Current direction unit vector
                   - 'ego_view' (ndarray): First-person camera view
               target: Target position (Vector) to navigate to
               
           Returns:
               str: Action command
           """
           position = obs['position']
           direction = obs['direction']
           ego_view = obs['ego_view']
           
           # Convert direction vector to yaw angle
           current_yaw = math.degrees(math.atan2(direction.y, direction.x))
           
           # Calculate the angle to target
           delta_x = target.x - position.x
           delta_y = target.y - position.y
           target_angle = math.degrees(math.atan2(delta_y, delta_x))
           
           # Calculate angle difference (normalized to [-180, 180])
           angle_diff = target_angle - current_yaw
           while angle_diff > 180:
               angle_diff -= 360
           while angle_diff < -180:
               angle_diff += 360
           
           prompt = f"""Current position: {position}
   Current direction: {direction} (direction vector, yaw: {current_yaw:.1f}°)
   Target position: {target}
   Distance to target: {position.distance(target):.1f}
   Angle to target: {angle_diff:.1f}° (positive = turn left, negative = turn right)

   Choose your next action to move closer to the target."""
           action, time = self.llm.generate_text(system_prompt=self.system_prompt, user_prompt=prompt)

           print(f"Raw response: {action}")
           return action.strip()

**Key features:**

- The agent receives observation containing position, direction vector, and ego-view camera image
- It calculates angle deviation to the target (positive = turn left, negative = turn right)
- The LLM outputs simple movement commands: "forward <duration>", "rotate <angle> <direction>", or "wait"

.. tip::

   To add memory or richer observations, extend this class and see :doc:`../components/agent_system` and :doc:`../components/unrealcv+`.

3. Build the environment wrapper
--------------------------------

The environment provides a Gym-like interface that manages the humanoid agent and executes actions:

.. code-block:: python

   class Environment:
       def __init__(self, communicator, config=Config()):
           self.communicator = communicator
           self.agent = None
           self.agent_name = None
           self.agent_spawned = False
           self.target = None
           self.config = config
           self.map = Map(config)
           self.map.initialize_map_from_file(
               roads_file=os.path.join('../data/example_city/demo_city_1/roads.json')
           )

       def reset(self):
           """Reset the humanoid to initial position and orientation."""
           agent_bp = "/Game/TrafficSystem/Pedestrian/Base_User_Agent.Base_User_Agent_C"
           spawn_location = Vector(0, 0)
           spawn_forward = Vector(1, 0)
           
           if not self.agent_spawned:
               # First time: Create and spawn the agent
               self.agent = Humanoid(
                   communicator=self.communicator,
                   position=spawn_location,
                   direction=spawn_forward,
                   config=self.config,
                   map=self.map
               )
               self.communicator.spawn_agent(
                   self.agent, name=None, model_path=agent_bp, type="humanoid"
               )
               self.communicator.humanoid_set_speed(self.agent.id, 200)
               self.agent_name = self.communicator.get_humanoid_name(self.agent.id)
               self.agent_spawned = True
           else:
               # Reset position and orientation
               location_3d = [spawn_location.x, spawn_location.y, 600]
               spawn_yaw = math.degrees(math.atan2(spawn_forward.y, spawn_forward.x))
               orientation_3d = [0, spawn_yaw, 0]
               
               self.communicator.unrealcv.set_location(location_3d, self.agent_name)
               self.communicator.unrealcv.set_orientation(orientation_3d, self.agent_name)
               self.agent.position = spawn_location
               self.agent.direction = spawn_yaw

           self.target = Vector(1700, -1700)
           time.sleep(5)

           # Get initial observation
           loc_3d = self.communicator.unrealcv.get_location(self.agent_name)
           position = Vector(loc_3d[0], loc_3d[1])
           
           orientation = self.communicator.unrealcv.get_orientation(self.agent_name)
           yaw = orientation[1]
           direction = Vector(math.cos(math.radians(yaw)), math.sin(math.radians(yaw)))
           
           ego_view = self.communicator.get_camera_observation(self.agent.camera_id, "lit")
           
           observation = {
               'position': position,
               'direction': direction,
               'ego_view': ego_view
           }
           return observation

       def step(self, action):
           """Parse and execute the action using humanoid movement functions."""
           action_cleaned = action.strip().strip('"').strip("'")
           action_lower = action_cleaned.lower().strip()
           success = False
           
           if action_lower.startswith("forward"):
               match = re.search(r'forward\s+(\d+\.?\d*)', action_lower)
               if match:
                   duration = float(match.group(1))
                   self.communicator.humanoid_step_forward(self.agent.id, duration, direction=0)
                   success = True
               else:
                   print(f"[Warning] Failed to parse forward action: '{action_cleaned}'")
               
           elif action_lower.startswith("rotate"):
               match = re.search(r'rotate\s+(\d+\.?\d*)\s+(left|right)', action_lower)
               if match:
                   angle = float(match.group(1))
                   direction = match.group(2)
                   self.communicator.humanoid_rotate(self.agent.id, angle, direction)
                   success = True
               else:
                   print(f"[Warning] Failed to parse rotate action: '{action_cleaned}'")
                   
           elif action_lower == "wait":
               time.sleep(1)
               success = True
           else:
               print(f"[Warning] Unknown action: '{action_cleaned}'")
               time.sleep(0.5)

           # Get current observation
           loc_3d = self.communicator.unrealcv.get_location(self.agent_name)
           position = Vector(loc_3d[0], loc_3d[1])
           
           orientation = self.communicator.unrealcv.get_orientation(self.agent_name)
           yaw = orientation[1]
           direction = Vector(math.cos(math.radians(yaw)), math.sin(math.radians(yaw)))

           self.agent.position = position
           self.agent.direction = yaw

           ego_view = self.communicator.get_camera_observation(self.agent.camera_id, "lit")

           observation = {
               'position': position,
               'direction': direction,
               'ego_view': ego_view
           }

           reward = -position.distance(self.target)
           return observation, reward, success

**Key features:**

- ``reset()`` spawns or resets the humanoid at origin and returns initial observation
- ``step(action)`` parses action strings and executes them via direct humanoid movement functions
- Observation is a dictionary with 'position', 'direction' (unit vector), and 'ego_view' (RGB image)
- Returns (observation, reward, success) where reward is negative distance to target

**Available movement functions:**

- ``humanoid_set_speed(humanoid_id, speed)``: Set movement speed
- ``humanoid_step_forward(humanoid_id, duration, direction)``: Move forward for duration seconds
- ``humanoid_rotate(humanoid_id, angle, direction)``: Rotate by angle degrees (left/right)

.. tip:: Customization Options

   - ``roads_file``: swap in your own map data for different layouts
   - ``agent_bp``: point to a different UE blueprint if you have custom characters
   - Adjust target position in ``reset()`` for different navigation tasks

4. Run a short rollout
----------------------

.. code-block:: python

   agent = Agent()
   env = Environment(communicator)

   obs = env.reset()

   print(f"Task: Navigate to target position {env.target}")
   print(f"Starting position: {obs['position']}\n")

   for i in range(100):
       # Agent decides next action based on current observation and target
       action = agent.action(obs, env.target)
       print(f"Step {i+1}: Action = '{action}'")
       
       # Execute action and get new observation
       obs, reward, success = env.step(action)
       
       # Only print details if action was successfully executed
       if success:
           position = obs['position']
           direction = obs['direction']
           
           current_yaw = math.degrees(math.atan2(direction.y, direction.x))
           
           # Calculate angle to target for display
           delta_x = env.target.x - position.x
           delta_y = env.target.y - position.y
           target_angle = math.degrees(math.atan2(delta_y, delta_x))
           angle_diff = target_angle - current_yaw
           while angle_diff > 180:
               angle_diff -= 360
           while angle_diff < -180:
               angle_diff += 360
           
           print(f"  Position: {position}, Direction: {direction} (yaw: {current_yaw:.1f}°)")
           print(f"  Reward: {reward:.2f}, Distance to target: {position.distance(env.target):.1f}")
           print(f"  Angle to target: {angle_diff:+.1f}° ({'turn left' if angle_diff > 0 else 'turn right'})\n")
           communicator.show_img(obs['ego_view'])
           
           # Check if reached target
           if position.distance(env.target) < 200:
               print(f"Target reached! Final position: {position}")
               break
       else:
           print(f"  [Action failed - skipping step]\n")

   communicator.disconnect()

You now have a minimal loop: observe the world (position, direction, ego-view), let the LLM suggest the next move, execute it via direct humanoid commands, and log rewards.

**What the agent does:**

1. Observes current position, direction vector, and ego-view camera image
2. Calculates angle deviation to target (helps decide whether to turn left or right)
3. Uses LLM to decide next action based on observation and distance to target
4. Executes action via humanoid movement functions
5. Receives reward based on negative distance to target (closer is better)

.. note::

   For more details on humanoid control and camera observations, see :doc:`../components/agent_system`, :doc:`../components/traffic_system`, and :doc:`../components/ue_detail`.

Next steps
----------

- Try different target positions or starting locations
- Implement more sophisticated reward functions or success criteria
- Incorporate different sensors for VLM-based agents; see :doc:`../components/ue_detail` for view modes and camera controls