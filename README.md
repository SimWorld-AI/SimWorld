# SimWorld: An Open-ended Realistic Simulator for Autonomous Agents in Physical and Social Worlds
<p align="center">
  <img src="https://github.com/user-attachments/assets/5d2da588-9470-44ef-82a9-5d45d592497a" width="840" height="795" alt="image" />
</p>


**SimWorld** is a simulation platform for developing and evaluating **LLM/VLM** AI agents in complex physical and social environments.

<div align="center">
    <a href="https://simworld-ai.github.io/"><img src="https://img.shields.io/badge/Website-SimWorld-blue" alt="Website" /></a>
    <a href="https://github.com/maitrix-org/SimWorld"><img src="https://img.shields.io/github/stars/maitrix-org/SimWorld?style=social" alt="GitHub Stars" /></a>
    <a href="https://simworld.readthedocs.io/en/latest"><img src="https://img.shields.io/badge/Documentation-Read%20Docs-green" alt="Documentation" /></a>
</div>

## 🔥 News
 - 2025.9 **SimWorld** has been accepted to NeurIPS 2025 main track as **spotlight** paper! 🎉
 - 2025.6 The first formal release of **SimWorld** has been published! 🚀
 - 2025.3 Our demo of **SimWolrd** been accepted by CVPR 2025 Demostration Tack! 🎉

## 💡 Introduction
SimWorld is built on Unreal Engine 5 and offers core capabilities to meet the needs of modern agent development. It provides:
- Realistic, open-ended world simulation with accurate physics and language-based procedural generation.
- Rich interface for LLM/VLM agents, supporting multi-modal perception and natural language actions.
- Diverse and customizable physical and social reasoning scenarios, enabling systematic training and evaluation of complex agent behaviors like navigation, planning, and strategic cooperation.

## 🏗️ Architecture
<p align="center">
    <img width="799" height="671" alt="image" src="https://github.com/user-attachments/assets/2e67356a-7dca-4eba-ab57-de1226e080bb" />
</p>

**SimWorld** consists of three layers:
- the Unreal Engine Backend, providing diverse and open-ended environments, rich assets and realistic physics simulation;
- the Environment layer, supporting procedural city generation, language-driven scene editing, gym-like APIs for LLM/VLM agents and traffic simulation;
- the Agent layer, enabling LLM/VLM agents to reason over multimodal observations and history while executing actions via an action planner;

SimWorld's architecture is designed to be modular and flexible, supporting an array of functionalities such as dynamic world generation, agent control, and performance benchmarking. The components are seamlessly integrated to provide a robust platform for **Embodied AI** and **Agents** research and applications.

### Project Structure
```bash
simworld/               # Python package
    local_planner/      # Local planner component
    agent/              # Agent system
    assets_rp/          # Live editor component for retrieval and re-placing
    citygen/            # City layout procedural generator
    communicator/       # Core component to connect Unreal Engine
    config/             # Configuration loader and default config file
    llm/                # Basic llm class
    map/                # Basic map class and waypoint system
    traffic/            # Traffic system
    utils/              # Utility functions
data/                   # Necessary input data
config/                 # Example configuration file and user configuration file
scripts/                # Examples of usage, such as layout generation and traffic simulation
docs/                   # Documentation source files
README.md
```

## Setup
### Installation
+ Python Client
Make sure to use Python 3.10 or later.
```bash
git clone https://github.com/renjw02/SimWorld.git
cd SimWorld
conda create -n simworld python=3.10
conda activate simworld
pip install -e .
```

+ UE server
Download the SimWorld server executable from S3:

    + Windows. Download the [SimWorld Windows 64-bit Server (v0.1.0)](https://simworld-release.s3.us-east-1.amazonaws.com/SimWorld-Win64-v0_1_0-Foundation.zip) and unzip it.
    + Linux. Download the [SimWorld Linux 64-bit Server (v0.1.0)](https://simworld-release.s3.us-east-1.amazonaws.com/SimWorld-Linux-v0_1_0-Foundation.zip) and unzip it.

### Quick Start

We provide several examples of code in `scripts/`, showcasing how to use the basic functionalities of SimWorld, including city layout generation, traffic simulation, asset retrieval, and activity-to-actions. Please follow the examples to see how SimWorld works.

#### Configuration

SimWorld uses YAML-formatted configuration files for system settings. The default configuration files are located in the `./simworld/config` directory while user configurations are placed in the `./config` directory.

- `./simworld/config/default.yaml` serves as the default configuration file.
- `./config/example.yaml` is provided as a template for custom configurations.

Users can switch between different configurations by specifying a custom configuration file path through the `Config` class:

To set up your own configuration:

1. Create your custom configuration by copying the example template:
   ```bash
   cp ./config/example.yaml ./config/your_config.yaml
   ```

2. Modify the configuration values in `your_config.yaml` according to your needs

3. Load your custom configuration in your code:
   ```python
   from simworld.config import Config
   config = Config('path/to/your_config')    # use absolute path here
   ```

#### Simple Running Example

Once the SimWorld UE5 environment is running, you can connect from Python and control an in-world humanoid agent in just a few lines:
(The whole example of minimal demo is shown in : [`examples/minimal_demo.ipynb`](https://github.com/SimWorld-AI/SimWorld/blob/hotfix-examples/examples/minimal_demo.ipynb))

```python
from simworld.communicator.unrealcv import UnrealCV
from simworld.communicator.communicator import Communicator
from simworld.agent.humanoid import Humanoid
from simworld.utils.vector import Vector
from simworld.llm.base_llm import BaseLLM


# Connect to the running Unreal Engine instance via UnrealCV
ucv = UnrealCV()
comm = Communicator(ucv)

class Agent:
    def __init__(self, goal):
        self.goal = goal
        self.llm = BaseLLM("gpt-4o")
        self.system_prompt = f"You are an intelligent agent in a 3D world. Your goal is to: {self.goal}."

    def action(self, obs):
        prompt = f"{self.system_prompt}\n You are currently at: {obs}\nWhat is your next action?"
        action = self.llm.generate_text(system_prompt=self.system_prompt, user_prompt=prompt)
        return action

class Environment:
    def __init__(self, comm: Communicator):
        self.comm = comm
        self.agent: Humanoid | None = None
        self.action_planner = None
        self.agent_name: str | None = None
        self.target: Vector | None = None

    def reset(self):
        """Clear the UE scene and (re)spawn the humanoid and target."""
        # Clear spawned objects
        self.comm.clear_env()

        # Blueprint path for the humanoid agent to spawn in the UE level
        agent_bp = "/Game/TrafficSystem/Pedestrian/Base_User_Agent.Base_User_Agent_C"

        # Initial spawn position and facing direction for the humanoid (2D)
        spawn_location, spawn_forward = Vector(0, 0), Vector(0, 1)
        self.agent = Humanoid(spawn_location, spawn_forward)
        self.action_planner = LocalPlanner(agent=self.agent,model=self.action_planner_llm,rule_based=False)

        # Spawn the humanoid agent in the Unreal world
        self.comm.spawn_agent(self.agent, name=None, model_path=agent_bp, type="humanoid")

        # Define a target position the agent is encouraged to move toward (example value)
        self.target = Vector(1000, 0)

        # Return initial observation (optional, but RL-style)
        observation = self.comm.get_camera_observation(self.agent.camera_id, "lit")

        return observation

    def step(self, action):
        """Use action planner to execute the given action."""
        # Parse the action text and map it to the action space
        primitive_actions = self.action_planner.parse(action)

        self.action_planner.execute(primitive_actions)

        # Get current location from UE (x, y, z) and convert to 2D Vector
        location = Vector(*self.comm.unrealcv.get_location(self.agent)[:2])

        # Camera observation for RL
        observation = self.comm.get_camera_observation(self.agent.camera_id, "lit")

        # Reward: negative Euclidean distance in 2D plane
        reward = -location.distance(self.target)

        return observation, reward


if __name__ == "__main__":
    # Create the environment wrapper
    agent = Agent(goal='Go to (1700, -1700) and pick up GEN_BP_Box_1_C.')
    env = Environment(communicator)

    obs = env.reset()

    # Roll out a short trajectory
    for _ in range(100):
        action = agent.action(obs)
        obs, reward = env.step(action)
        print(f"obs: {obs}, reward: {reward}")
        # Plug this into your RL loop / logging as needed
```


## For Contributors
### Precommit Setup

We use Google docstring format for our docstrings and the pre-commit library to check our code. To install pre-commit, run the following command:

```bash
conda install pre-commit  # or pip install pre-commit
pre-commit install
```

The pre-commit hooks will run automatically when you try to commit changes to the repository.


### Commit Message Guidelines
All commit messages should be clear, concise, and follow this format:
```
<type>: <short summary>

[optional body explaining the change]
```
Recommended types:
+ feat: A new feature
+ fix: A bug fix
+ docs: Documentation changes
+ refactor: Code restructuring without behavior changes
+ style: Code style changes (formatting, linting)
+ test: Adding or updating tests
+ chore: Non-code changes (e.g., updating dependencies)

Example:
```
feat: add user login API
```

### Issue Guidelines
+ Use clear titles starting with [Bug] or [Feature].
+ Describe the problem or request clearly.
+ Include steps to reproduce (for bugs), expected behavior, and screenshots if possible.
+ Mention your environment (OS, browser/runtime, version, etc.).

### Pull Request Guidelines
+ Fork the repo and create a new branch (e.g., feature/your-feature, fix/bug-name).
+ Keep PRs focused: one feature or fix per PR.
+ Follow the project’s coding style and naming conventions.
+ Test your changes before submitting.
+ Link related issues using Fixes #issue-number if applicable.
+ Add comments or documentation if needed.

We appreciate clean, well-described contributions! 🚀
