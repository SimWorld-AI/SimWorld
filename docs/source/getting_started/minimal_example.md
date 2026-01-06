# Minimal Example

Walk through the `examples/gym_interface_demo.ipynb` notebook with a step-by-step setup. This example launches a simple LLM-driven humanoid that plans in natural language and executes via the Local Planner.

## Prerequisites
- Install the Python client and have the UE backend running (see [Installation](../getting_started/installation.md)).
- Ensure the backend is reachable (default ports 9000). If you changed ports, pass them through command line arguments `--cvport 9001` or change the `/gym_citynav/Binaries/Win64/unrealcv.ini`.
- Set an OpenAI-compatible API key in your environment (the demo uses `gpt-4o` for the agent and `gpt-4o-mini` for the planner).

```bash
export OPENAI_API_KEY="<your_api_key>"
```

```{note}
You can swap models or providers by changing `BaseLLM` / `A2ALLM` parameters. See [Agent System](../components/agent_system.md) for interfaces.
```

## 1. Import and configure
```python
import sys
from pathlib import Path

sys.path.append(str(Path().resolve().parent))  # make repo importable

from simworld.config import Config
from simworld.communicator.communicator import Communicator
from simworld.communicator.unrealcv import UnrealCV
from simworld.llm.base_llm import BaseLLM
from simworld.llm.a2a_llm import A2ALLM
from simworld.map.map import Map
from simworld.agent.humanoid import Humanoid
from simworld.utils.vector import Vector
from simworld.local_planner.local_planner import LocalPlanner
```

Create the communicator to talk to the UE backend:
```python
communicator = Communicator(UnrealCV())
```

## 2. Define a simple LLM agent
```python
class Agent:
    def __init__(self, goal):
        self.goal = goal
        self.llm = BaseLLM("gpt-4o")
        self.system_prompt = f"You are an intelligent agent in a 3D world. Your goal is to: {self.goal}."

    def action(self, obs):
        prompt = f"{self.system_prompt}\n You are currently at: {obs}\nWhat is your next goal?"
        return self.llm.generate_text(system_prompt=self.system_prompt, user_prompt=prompt)
```

```{tip}
To add memory or richer observations, extend this class and see [Agent System](../components/agent_system.md) and [UnrealCV+ details](../components/unrealcv+.md).
```

## 3. Build the environment wrapper
```python
import os

class Environment:
    def __init__(self, communicator, config=Config()):
        self.communicator = communicator
        self.config = config
        self.action_planner_llm = A2ALLM(model_name="gpt-4o-mini")
        self.map = Map(config)
        self.map.initialize_map_from_file(roads_file="../data/sample_data/road.json")

    def reset(self):
        self.communicator.clear_env()

        agent_bp = "/Game/TrafficSystem/Pedestrian/Base_User_Agent.Base_User_Agent_C"
        spawn_location = Vector(0, 0)
        spawn_forward = Vector(0, 1)

        self.agent = Humanoid(
            communicator=self.communicator,
            position=spawn_location,
            direction=spawn_forward,
            config=self.config,
            map=self.map,
        )

        self.action_planner = LocalPlanner(
            agent=self.agent,
            model=self.action_planner_llm,
            rule_based=False,
        )

        self.communicator.spawn_agent(
            self.agent, name=None, model_path=agent_bp, type="humanoid"
        )
        self.agent_name = self.communicator.get_humanoid_name(self.agent.id)

        self.target = Vector(1000, 0)
        return self.communicator.unrealcv.get_location(self.agent_name)

    def step(self, action):
        primitive_actions = self.action_planner.parse(action)
        self.action_planner.execute(primitive_actions)

        loc_3d = self.communicator.unrealcv.get_location(self.agent_name)
        location = Vector(loc_3d[0], loc_3d[1])
        reward = -location.distance(self.target)
        return location, reward
```

Key things to customize:
- `roads_file`: swap in your own map data for different layouts.
- `agent_bp`: point to a different UE blueprint if you have custom characters.
- `rule_based`: set to `True` to use deterministic navigation; see [Local Planner](../components/agent_system.md).

## 4. Run a short rollout
```python
agent = Agent(goal="Go to (1700, -1700) and pick up GEN_BP_Box_1_C.")
env = Environment(communicator)

obs = env.reset()

for _ in range(100):
    action = agent.action(obs)
    obs, reward = env.step(action)
    print(f"obs: {obs}, reward: {reward}")

communicator.disconnect()
```

You now have a minimal loop: observe the world, let the LLM suggest the next move, execute it through the Local Planner, and log rewards.

```{note}
For action space details and planner behavior, read [Agent System](../components/agent_system.md), [Traffic System](../components/traffic_system.md), and [Actions](../components/ue_detail.md).
```

## Next steps
- Try different goals or shorter loops to debug.
- Replace `A2ALLM` with your own model wrapper for planning.
- Incorporate image observations via `UnrealCV.get_image` for VLM-based agents; see [Sensors](../components/ue_detail.md) for view modes and camera controls.
