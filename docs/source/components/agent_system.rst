Agent System
============

Overview
--------
To support the development and evaluation of LLM/VLM-driven agents, SimWorld offers a robust and scalable **Agent System**. Specifically, SimWorld defines two categories of agents:

+ Rule-based agents: Serve as background entities (e.g., vehicles and pedestrians) to create a more realistic environment. See the :doc:`Traffic System <traffic_system>` for details.

+ LLM/VLM-driven agents: Designed for researchers exploring AI agent behavior, multi-agent interactions, NLP tasks, and embodied AI research.

Base Agent
----------
SimWorld provides a foundational class ``BaseAgent`` for all types of agents. This class encapsulates the agent's physical state in Unreal Engine, including its position and direction (yaw). Users can create custom agents by inheriting from ``BaseAgent``.

.. code-block:: python

    class BaseAgent:
        def __init__(self, position: Vector, direction: Vector):
            """Initialize the base agent.

            Args:
                position: Initial position vector.
                direction: Initial direction vector.
            """
            self._position = position
            self._direction = direction
            self._yaw = 0

For LLM/VLM integration, SimWorld provides a basic LLM interface (:ref:`Base LLM <base-llm>`).

**Related files:** ``agent/base_agent.py``.

.. _base-llm:

Base LLM
--------
SimWorld provides a ``BaseLLM`` class as a foundational interface for LLMs into the framework. It is designed to be extensible and robust, with automatic retry mechanisms built into all public methods to improve reliability when interacting with external APIs.

.. code-block:: python

    class BaseLLM(metaclass=LLMMetaclass):
        def __init__(
            self,
            model_name: str,
            url: Optional[str] = None,
            provider: Optional[str] = 'openai'
        ):
        ...

This class serves as the base class for custom LLM implementations, supporting common providers such as OpenAI by default. Developers can extend it to integrate models hosted locally or through other third-party services.

.. note::
    Currently SimWorld only supports OpenAI and OpenRouter API calls.

**Related files:** ``llm/base_llm.py``.

Get Camera Observation
----------------------
After initializing the agent, the image observation can be obtained by calling the ``get_image(camera_id)`` method.

.. code-block:: python

    unrealcv = UnrealCV()
    unrealcv.connect()

    agent = Humanoid(position=Vector(0, 0), direction=Vector(0, 1))

    observation = unrealcv.get_image(camera_id=agent.camera_id)

``camera_id`` refers to the index of the camera associated with an agent. It is typically determined by the order in which cameras are generated, starting from 1 for the first agent that includes a camera. Currently, each vehicle, pedestrian, humanoid, and robot dog is assigned a camera.

.. note::
    Currently, SimWorld only supports one camera per agent.

    The resolution of the image is default to (640, 480). To customize, you can use the ``set_camera_resolution()`` to set the resolution.

Check :doc:`UnrealCV <../resources/simworld.communicator>` and :ref:`Unreal Engine Backend Sensors <ue_detail-sensors>` to see more details.

Action Space
------------
SimWorld defines a two-tiered action space to support hierarchical planning and execution: ``HighLevelAction`` and ``LowLevelAction``.

+ High-level actions represent abstract tasks and are intended to be parsed from natural language inputs by the parser module in the **Local Planner**.

+ Low-level actions particularly correspond to navigation-related actions.

See the complete action tables below for a full overview of supported actions across different agent types.

.. code-block:: python

    class HighLevelAction(Enum):
        """High-level actions that an agent can perform."""
        DO_NOTHING = 0
        NAVIGATE = 1
        PICK_UP = 2
        ...

    class LowLevelAction(Enum):
        """Low-level actions that an agent can perform."""
        DO_NOTHING = 0
        STEP_FORWARD = 1
        TURN_AROUND = 2

This modular design encourages extensibility and users are welcome to define custom actions to suit task-specific needs.

**Related files:** ``local_planner/action_space.py``.

Complete Action Reference
~~~~~~~~~~~~~~~~~~~~~~~~~

The following table provides a comprehensive overview of all actions available in SimWorld across different agent types:

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 15 35

   * - **Action**
     - **Agent Type**
     - **Category**
     - **Control Mode**
     - **Description**
   * - **High-Level Actions**
     - 
     - 
     - 
     - 
   * - Do Nothing
     - All
     - System
     - Discrete
     - Perform no action for one time step
   * - Navigate
     - All
     - Navigation
     - Discrete
     - Navigate to a specified destination using pathfinding
   * - Pick Up
     - Humanoid
     - Object Interaction
     - Discrete
     - Grasp and lift an object
   * - **Low-Level Actions**
     - 
     - 
     - 
     - 
   * - Do Nothing
     - All
     - System
     - Discrete
     - Perform no action for one time step
   * - Step Forward
     - All
     - Navigation
     - Discrete
     - Move forward for a fixed time duration
   * - Turn Around
     - All
     - Navigation
     - Discrete
     - Rotate 180 degrees to face the opposite direction
   * - **Humanoid Actions**
     - 
     - 
     - 
     - 
   * - Move Forward
     - Humanoid
     - Navigation
     - Continuous
     - Keep moving in the current direction
   * - Step Forward/Backward
     - Humanoid
     - Navigation
     - Discrete
     - Step forward/backward for a fixed time
   * - Rotate
     - Humanoid
     - Navigation
     - Discrete
     - Turn the body to face a new direction
   * - Stop
     - Humanoid
     - Navigation
     - Discrete
     - Stop moving
   * - Look Up/Down
     - Humanoid
     - Observation
     - Discrete
     - Adjust the gaze upward/downward by a degree
   * - Focus
     - Humanoid
     - Observation
     - Discrete
     - Adjust the field of view
   * - Drop Off
     - Humanoid
     - Object Interaction
     - Discrete
     - Release a held object at the target location
   * - Sit Down
     - Humanoid
     - Object Interaction
     - Discrete
     - Transition to a seated position
   * - Stand Up
     - Humanoid
     - Object Interaction
     - Discrete
     - Rise from a seated position
   * - Enter Car
     - Humanoid
     - Object Interaction
     - Discrete
     - Get into a vehicle
   * - Exit Car
     - Humanoid
     - Object Interaction
     - Discrete
     - Leave a vehicle
   * - Get On Scooter
     - Humanoid
     - Object Interaction
     - Discrete
     - Get on a scooter
   * - Get Off Scooter
     - Humanoid
     - Object Interaction
     - Discrete
     - Get off a scooter
   * - Have Conversation
     - Humanoid
     - Social Action
     - Discrete
     - Exchange verbal communication
   * - Point Direction
     - Humanoid
     - Social Action
     - Discrete
     - Gesture to indicate direction
   * - Wave Hand
     - Humanoid
     - Social Action
     - Discrete
     - Signal or greet with a hand wave
   * - Discuss
     - Humanoid
     - Social Action
     - Discrete
     - Engage in dialogue or explanation
   * - Argue with Body Language
     - Humanoid
     - Social Action
     - Discrete
     - Express disagreement using gestures
   * - **Vehicle Actions**
     - 
     - 
     - 
     - 
   * - Set Throttle/Brake/Steering
     - Vehicle
     - Driving
     - Continuous
     - Control a vehicle's acceleration, braking, and steering
   * - **Robot Dog Actions**
     - 
     - 
     - 
     - 
   * - Transition
     - Robot Dog
     - Movement
     - Continuous/Discrete
     - Move in specified direction with controllable step length and speed
   * - Rotation
     - Robot Dog
     - Movement
     - Continuous/Discrete
     - Rotate around vertical axis with controllable angle and speed
   * - Look Up
     - Robot Dog
     - Observation
     - Discrete
     - Tilt the robot's head upward to change camera view
   * - Look Down
     - Robot Dog
     - Observation
     - Discrete
     - Tilt the robot's head downward to change camera view
   * - Hold Position
     - Robot Dog
     - Movement
     - Continuous/Discrete
     - Keep the robot still in current pose for specified duration

.. note::
    Robot Dog actions support both continuous and discrete control modes except for Look Up/Down actions, which are discrete only. The transition and rotation actions allow fine-grained control over parameters like step length, movement speed, rotation angle, and direction.

Demo for human action space
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Initialize a humanoid agent with position (0, 0) and facing direction (1, 0)
   humanoid = Humanoid(Vector(0, 0), Vector(1, 0))
   humanoid_name = 'GEN_BP_Humanoid_0'

   # Spawn the humanoid in the simulator using the specified model path
   communicator.spawn_agent(humanoid, humanoid_model_path)

   # Make the humanoid sit down
   ucv.humanoid_sit_down(humanoid_name)

   # Make the humanoid stand up
   ucv.humanoid_stand_up(humanoid_name)

   # Play an "argue" animation (the number may represent the type or intensity)
   ucv.humanoid_argue(humanoid_name, 0)

   # Play a "discuss" animation
   ucv.humanoid_discuss(humanoid_name, 0)

   # Play a "listening" animation
   ucv.humanoid_listen(humanoid_name)

   # Make the humanoid point or gesture along a path
   ucv.humanoid_directing_path(humanoid_name)

   # Play a waving gesture directed toward a dog
   ucv.humanoid_wave_to_dog(humanoid_name)

   # Make the humanoid pick up an object (e.g., a mug)
   ucv.humanoid_pick_up_object(humanoid_name, "BP_Mug_C_1")

   # Drop the currently held object
   ucv.humanoid_drop_object(humanoid_name)

   # Command the humanoid to enter a specific vehicle
   ucv.humanoid_enter_vehicle(humanoid_name, "BP_VehicleBase_Destruction_C_1")

   # Command the humanoid to exit that vehicle
   ucv.humanoid_exit_vehicle(humanoid_name, "BP_VehicleBase_Destruction_C_1")

   # Create a scooter object at position (100, 0) facing direction (0, 1)
   scooter = Scooter(Vector(100, 0), Vector(0, 1))

   # Spawn the scooter into the simulation
   communicator.spawn_scooter(scooter, scooter_path)

   # Make the humanoid get on the scooter
   communicator.humanoid_get_on_scooter(agent.id)

   # Set scooter attributes: speed = 0.5, direction = 0, angular velocity = 0
   communicator.set_scooter_attributes(agent.scooter_id, 0.5, 0, 0)

   # Make the humanoid get off the scooter
   communicator.humanoid_get_off_scooter(agent.id, scooter.id)

   # Make the humanoid step forward for 2 seconds
   communicator.humanoid_step_forward(agent.id, 2)

   # Rotate the humanoid 90 degrees to the left
   communicator.humanoid_rotate(agent.id, 90, 'left')

   # Start continuous forward movement
   communicator.humanoid_move_forward(agent.id)

   # Stop movement, optionally play a stop animation for 2 seconds
   communicator.humanoid_stop(agent.id, 2)

Demo for robot action space
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Specify robot name and asset
    robot_name = "Demo_Robot"
    robot_asset = "/Game/Robot_Dog/Blueprint/BP_SpotRobot.BP_SpotRobot_C"

    # Spawn robot in the simulator
    ucv.spawn_bp_asset(robot_asset, robot_name)
    ucv.enable_controller(robot_name, True)

    # Robot - look up / look down
    ucv.dog_look_up(robot_name)    # look up
    ucv.dog_look_down(robot_name)  # look down

    # Robot Movement
    # direction: 0 = forward, 1 = backward, 2 = left, 3 = right
    for direction in [0, 1, 2, 3]:
        speed = 200
        duration = 1
        move_parameter = [speed, duration, direction]
        ucv.dog_move(robot_name, move_parameter)
        time.sleep(duration)

    # Robot Rotation
    # clockwise: 1 = right turn, -1 = left turn
    for angle, clockwise in [(90, 1), (-90, -1)]:
        duration = 0.7
        rotate_parameter = [duration, angle, clockwise]
        ucv.dog_rotate(robot_name, rotate_parameter)
        time.sleep(duration)

See :doc:`SimWorld-Robotics <../simworld-robotics/simworld_robotics>` for more details.

Demo for vehicle action space
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Specify vehicle name and asset
    vehicle_name = "Demo_Vehicle"
    vehicle_asset = "/Game/TrafficSystem/Vehicle/Vehicle1.Vehicle1_C"

    # Spawn vehicle in the simulator
    ucv.spawn_bp_asset(vehicle_asset, vehicle_name)
    ucv.enable_controller(vehicle_name, True)

    # Set vehicle throttle, brake, and steering
    throttle = 0.5  # Throttle value between 0.0 and 1.0
    brake = 0.0     # Brake value between 0.0 and 1.0
    steering = 0.1  # Steering value between -1.0 (left) and 1.0 (right)
    ucv.v_set_state(vehicle_name, throttle, brake, steering)

    # Let the vehicle make a U turn
    ucv.v_make_u_turn(vehicle_name)


**Related files:** ``communicator.py``, ``unrealcv.py``.

A complete example can be found in ``examples/ue_command.ipynb``.

Local Planner
-------------
To accommodate diverse research focuses—ranging from text-based LLM agents to vision-based VLM agents—SimWorld introduces a flexible and modular **Local Planner** to bridge high-level reasoning with low-level execution. The core functionality of the Local Planner lies in its ability to decompose abstract plans into concrete, executable actions, enabling seamless integration between language, vision, and simulation.

The Local Planner consists of two main components: the parser and the executor.

+ The parser takes a high-level plan described in natural language and breaks it down into a sequence of low-level actions. This plan can originate either from human input or from upstream LLM/VLM modules.

+ The executor then interprets and performs these low-level actions within the simulated environment. For non-atomic tasks such as navigation, the executor supports two operational modes:

    + Rule-based mode: Agents follow a predefined route generated by the A* algorithm.

    + Vision-based mode: Agents rely solely on visual inputs and the goal destination, making decisions using a VLM-driven policy.

The Local Planner is designed with extensibility and modularity in mind. Users can plug in their own LLMs/VLMs via API calls, and customize either component independently. This decoupling allows researchers to focus on specific layers of cognition or perception without needing to manage the full control pipeline.

In summary, the Local Planner serves as a crucial abstraction layer that decouples high-level social reasoning from low-level physical execution, empowering users to design and experiment with custom agent architectures (e.g., observation models, memory systems, or reasoning engines) tailored to their research needs.

**Related files:** ``local_planner/local_planner.py``.

Demo for using Local Planner
~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Local Planner should be used with an agent.

.. code-block:: python

    # Initialize the local planner
    local_planner = LocalPlanner(agent=humanoid, model=llm, rule_based=False)

.. code-block:: python

    # Parse high level plan
    plan = 'Go to (1700, -1700) and pick up GEN_BP_Bottle_1_C.'
    action_space = local_planner.parse(plan)

.. code-block:: python

    # Execution
    local_planner.execute(action_space)

A complete example can be found in ``examples/local_action_planner.ipynb``.

Agent Asset Paths
------------------

The following table lists the asset paths for different agent types available in SimWorld. These paths are used when spawning agents in Unreal Engine through the communicator.

.. list-table::
   :header-rows: 1
   :widths: 15 45 40

   * - Agent Type
     - Asset Path
     - Description
   * - Vehicle
     - ``/Game/TrafficSystem/Vehicle/Base_Vehicle.Base_Vehicle``
     - Base vehicle template
   * - Vehicle
     - ``/Game/TrafficSystem/Vehicle/Vehicle1.Vehicle1``
     - Vehicle variant 1
   * - Vehicle
     - ``/Game/TrafficSystem/Vehicle/Vehicle2.Vehicle2``
     - Vehicle variant 2
   * - Vehicle
     - ``/Game/TrafficSystem/Vehicle/Vehicle3.Vehicle3``
     - Vehicle variant 3
   * - Vehicle
     - ``/Game/TrafficSystem/Vehicle/Vehicle4.Vehicle4``
     - Vehicle variant 4
   * - Vehicle
     - ``/Game/TrafficSystem/Vehicle/Vehicle5.Vehicle5``
     - Vehicle variant 5
   * - Robot Dog
     - ``/Game/Robot_Dog/Blueprint/BP_SpotRobot.BP_SpotRobot``
     - Boston Dynamics Spot-like robot
   * - Humanoid
     - ``/Game/TrafficSystem/Pedestrian/Base_Pedestrian.Base_Pedestrian``
     - Base pedestrian template
   * - Humanoid
     - ``/Game/TrafficSystem/Pedestrian/Base_User_Agent.Base_User_Agent``
     - User-controllable humanoid agent

Usage
~~~~~
These asset paths are used with the communicator's ``spawn_agent()`` method:

.. code-block:: python

    # Example: Spawn a humanoid agent
    communicator.spawn_agent(
        agent=humanoid_agent,
        model_path="/Game/TrafficSystem/Pedestrian/Base_Pedestrian.Base_Pedestrian_C",
        type="humanoid"
    )

.. important::
    **Model Path Convention**: When using these paths programmatically, you must append ``_C`` to the asset path. This is the Unreal Engine convention for compiled blueprint classes.

    Examples:

    - Asset Path: ``/Game/TrafficSystem/Vehicle/Base_Vehicle.Base_Vehicle``
    - Model Path: ``/Game/TrafficSystem/Vehicle/Base_Vehicle.Base_Vehicle_C``

Related Documentation
~~~~~~~~~~~~~~~~~~~~~
- For detailed spawning procedures, see :doc:`UnrealCV+ <unrealcv+>`