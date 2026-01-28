# SimWorld: An Open-ended Realistic Simulator for Autonomous Agents in Physical and Social Worlds
<p align="center">
  <img src="https://github.com/user-attachments/assets/5d2da588-9470-44ef-82a9-5d45d592497a" width="840" height="795" alt="image" />
</p>


**SimWorld** is a simulation platform for developing and evaluating **LLM/VLM** AI agents in complex physical and social environments.

<div align="center">
    <a href="https://simworld-ai.github.io/"><img src="https://img.shields.io/badge/Website-SimWorld-blue" alt="Website" /></a>
    <a href="https://github.com/maitrix-org/SimWorld"><img src="https://img.shields.io/github/stars/maitrix-org/SimWorld?style=social" alt="GitHub Stars" /></a>
    <a href="https://simworld.readthedocs.io/en/latest"><img src="https://img.shields.io/badge/Documentation-Read%20Docs-green" alt="Documentation" /></a>
    <a href="https://arxiv.org/abs/2512.01078"><img src="https://img.shields.io/badge/arXiv-2512.01078-b31b1b?logo=arxiv&logoColor=white" alt="arXiv:2512.01078" /></a>
</div>

## 🎬 Demonstration
<!-- <p align="center">
  <a href="https://youtu.be/-e19MzwDhy4" target="_blank" rel="noopener noreferrer">
    <img
      src="https://img.youtube.com/vi/-e19MzwDhy4/0.jpg"
      alt="SimWorld Demo Video"
    />
  </a>
</p> -->
<p align="center">
  <a href="https://www.youtube.com/watch?v=SfOifXTupgY" target="_blank" rel="noopener noreferrer">
    <img
      src="docs/source/assets/video_cover.jpg"
      alt="SimWorld Demo Video"
    />
  </a>
</p>

<p align="center">
  <a href="https://www.youtube.com/@SimWorld-AI" target="_blank" rel="noopener noreferrer">
    ▶ See all our demo videos on YouTube
  </a>
</p>

## 🔥 News
 - 2026.1 **SimWorld** now supports importing customized environments and agents([doc](https://simworld.readthedocs.io/en/latest/customization/make_your_own_pak.html))!
 - 2025.11 The [white paper](https://simworld.org/assets/white_paper.pdf) of **SimWorld** is available on arxiv!
 - 2025.9 **SimWorld** has been accepted to NeurIPS 2025 main track as a **spotlight** [paper](https://neurips.cc/virtual/2025/loc/san-diego/poster/119002)! 🎉
 - 2025.6 The first formal [release](https://x.com/Lianhuiq/status/1995585268121002381?s=20) of **SimWorld** has been published! 🚀
 - 2025.3 Our [demo](https://www.youtube.com/@SimWorld-AI) of **SimWorld** has been accepted by CVPR 2025 Demonstration Track! 🎉

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
- the Agent layer, enabling LLM/VLM agents to reason over multimodal observations and history while executing actions via a local action planner.

SimWorld's architecture is designed to be modular and flexible, supporting an array of functionalities such as dynamic world generation, agent control, and performance benchmarking. The components are seamlessly integrated to provide a robust platform for **Embodied AI** and **Agents** research and applications.

### Project Structure
```bash
simworld/               # Python package
    local_planner/      # Local action planner component
    agent/              # Agent system
    assets_rp/          # Live editor component for retrieval and re-placing
    citygen/            # City layout procedural generator
    communicator/       # Core component to connect Unreal Engine
    config/             # Configuration loader and default config file
    llm/                # Basic llm class
    map/                # Basic map class and waypoint system
    traffic/            # Traffic system
    utils/              # Utility functions
    data/               # Default data files, e.g., object categories
    weather/            # Weather system
data/                   # Necessary input data
config/                 # Example configuration file and user configuration file
examples/                # Examples of usage, such as layout generation and traffic simulation
docs/                   # Documentation source files
README.md
```

## ⚙️ Setup

This section walks through the minimal setup to run SimWorld using our provided UE packages and the Python client. If you want to use your own custom environments, assets, or agent models, you can import them via `.pak` files. See [Make Your SimWorld](#make-your-simworld) for instructions.

**System Requirements:** SimWorld requires Windows or Linux operating system, a dedicated GPU with ≥6GB VRAM, 32GB RAM, and 50-200GB disk space depending on the package. For detailed hardware requirements and recommendations, see the [Device Requirement](https://simworld.readthedocs.io/en/latest/getting_started/installation.html).


### Installation
#### Step 1. Install the Python Client

Make sure to use Python 3.10 or later.
```bash
git clone https://github.com/SimWorld-AI/SimWorld.git
cd SimWorld
conda create -n simworld python=3.10
conda activate simworld
pip install -e .
```

#### Step 2. Download the UE Server Package

First, download and extract the **Base** UE server package for your OS. The Base package includes two lightweight city scenes and one empty map for quickly testing SimWorld’s core features, including core agent interaction and procedural city generation.

- **Base (required, 2 city maps and 1 empty map)**
  - **Windows:** [Download](https://huggingface.co/datasets/SimWorld-AI/SimWorld/blob/main/Base/Windows.zip)
  - **Linux:** [Download](https://huggingface.co/datasets/SimWorld-AI/SimWorld/blob/main/Base/Linux.zip)

If you want more pre-built scenes for demos and diverse scenarios, you can optionally install **Additional Environments (100+ Maps)**. This is an add-on map pack that extends the Base installation. Download the maps you need and copy the `.pak` files into the Base server folder at:
`SimWorld/Content/Paks/`.

- **Additional Environments (optional, 100+ maps)**
  - **Windows:** [Download](https://huggingface.co/datasets/SimWorld-AI/SimWorld/tree/main/AdditionEnvironmentPaks/Windows)
  - **Linux:** [Download](https://huggingface.co/datasets/SimWorld-AI/SimWorld/tree/main/AdditionEnvironmentPaks/Linux)

The Additional Environments package is organized as separate `.pak` files, so you can download only the maps you need. Please check the [download and installation](https://simworld.readthedocs.io/en/latest/getting_started/additional_environments.html#download-and-installation) for usage instructions, including how to load specific maps and what each `.pak` contains.


### Quick Start

We provide several examples of code in [examples/](examples/), showcasing how to use the basic functionalities of SimWorld, including city layout generation, traffic simulation, asset retrieval, and activity-to-actions. Please follow the examples to see how SimWorld works.

#### Step 1. Start the UE Server
Start the SimWorld UE server first, then run the Python examples. From the extracted UE server package directory:

- **Windows:** double-click `SimWorld.exe`, or launch it from the command line:
  ```bash
  ./SimWorld.exe <MAP_PATH>
  ```

- **Linux:** run:
    ```bash
    ./SimWorld.sh <MAP_PATH>
    ```

`<MAP_PATH>` refers to the Unreal Engine internal path to a map file (e.g., `/Game/hospital/map/demo.umap`). SimWorld's **base** binary contains 2 city maps and 1 empty map. See [Base Environments](https://simworld.readthedocs.io/en/latest/getting_started/base_environments.html) for details. In addition, users can download 100+ **additional environment paks**. See the [Additional Environments](https://simworld.readthedocs.io/en/latest/getting_started/additional_environments.html) for the installation and complete list of available map paths. If `<MAP_PATH>` is not specified, the default map (`/Game/Maps/demo_1`) will be open.

#### Step 2. Run a Minimal Gym-Style Example

Once the SimWorld UE5 environment is running, you can connect from Python and control an in-world humanoid agent in just a few lines. The full demo is provided in [examples/gym_interface_demo.ipynb](examples/gym_interface_demo.ipynb). You can also run other example scripts/notebooks under [examples/](examples/).

```python
from simworld.communicator.unrealcv import UnrealCV
from simworld.communicator.communicator import Communicator
from simworld.agent.humanoid import Humanoid
from simworld.utils.vector import Vector
from simworld.llm.base_llm import BaseLLM
from simworld.local_planner.local_planner import LocalPlanner
from simworld.llm.a2a_llm import A2ALLM

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
        self.action_planner_llm = A2ALLM(model_name="gpt-4o-mini")

    def reset(self):
        """Clear the UE scene and (re)spawn the humanoid and target."""
        # Clear spawned objects
        self.comm.clear_env()

        # Blueprint path for the humanoid agent to spawn in the UE level
        agent_bp = "/Game/TrafficSystem/Pedestrian/Base_User_Agent.Base_User_Agent_C"

        # Initial spawn position and facing direction for the humanoid (2D)
        spawn_location, spawn_forward = Vector(0, 0), Vector(0, 1)
        self.agent = Humanoid(spawn_location, spawn_forward)
        self.action_planner = LocalPlanner(agent=self.agent, model=self.action_planner_llm, rule_based=False)

        # Spawn the humanoid agent in the Unreal world
        self.comm.spawn_agent(self.agent, name=None, model_path=agent_bp, type="humanoid")

        # Define a target position the agent is encouraged to move toward (example value)
        self.target = Vector(1700, -1700)

        # Return initial observation (optional, but RL-style)
        observation = self.communicator.unrealcv.get_location(self.agent_name)
        ret = Vector(observation[0], observation[1])
        return ret

    def step(self, action):
        """Use action planner to execute the given action."""
        # Parse the action text and map it to the action space
        primitive_actions = self.action_planner.parse(action)

        self.action_planner.execute(primitive_actions)

        # Get current location from UE (x, y, z) and convert to 2D Vector
        location = Vector(*self.comm.unrealcv.get_location(self.agent)[:2])

        observation = location
        self.agent.position = location

        # Reward: negative Euclidean distance in 2D plane
        reward = -location.distance(self.target)

        return observation, reward

if __name__ == "__main__":
    # Connect to the running Unreal Engine instance via UnrealCV
    ucv = UnrealCV()
    comm = Communicator(ucv)

    # Create the environment wrapper
    agent = Agent(goal='Go to (1700, -1700).')
    env = Environment(comm)

    obs = env.reset()

    # Roll out a short trajectory
    for _ in range(100):
        action = agent.action(obs)
        obs, reward = env.step(action)
        print(f"obs: {obs}, reward: {reward}")
        # Plug this into your RL loop / logging as needed
```

## 📚 Configuration and API Reference

### Configuration

SimWorld uses a YAML configuration file to control **global simulator settings** (e.g., `seed`, `dt`, UE blueprint paths) and **module behaviors** (e.g., city generation, traffic simulation, asset retrieval, and agent/LLM options).

For a comprehensive reference of all configuration parameters, see the [Configuration Reference](https://simworld.readthedocs.io/en/latest/getting_started/configuration.html) documentation.

We provide two configuration files to help you get started:
- [simworld/config/default.yaml](simworld/config/default.yaml) contains the **built-in defaults** shipped with the package (reference/fallback). We recommend **not editing** this file.
- [config/example.yaml](config/example.yaml) is a **user template** with placeholders for local paths. Copy it to create your own config.

If you want to customize SimWorld for your own setup, follow the steps below to create and load your own config:

1. Create a custom config from the template:
   ```bash
   cp config/example.yaml config/your_config.yaml
   ```

2. Modify the configuration values in `your_config.yaml` according to your needs.

3. Load your custom configuration in your code:
   ```python
   from simworld.config import Config
   config = Config('path/to/your_config')    # use absolute path here
   ```

### API and Usage

#### Agent Action Space
SimWorld provides a comprehensive action space for pedestrians, vehicles, and robots (e.g., move forward, sit down, pick up). For more details, see [actions](https://simworld.readthedocs.io/en/latest/components/agent_system.html#action-space) and [examples/ue_command.ipynb](examples/ue_command.ipynb).

#### Using UE Cameras and Sensors
SimWorld supports a variety of sensors, including RGB images, segmentation maps, and depth images. For more details, please refer to the [sensors](https://simworld.readthedocs.io/en/latest/components/ue_detail.html#sensors) and the example script [examples/camera.ipynb](examples/camera.ipynb).

#### Commonly Used APIs
All APIs are located in [simworld/communicator](simworld/communicator). Some of the most commonly used ones are listed below:
- [communicator.get_camera_observation](simworld/communicator/communicator.py#L195) (Get camera images: RGB, depth, or segmentation mask)
- [communicator.spawn_object](simworld/communicator/communicator.py#L574) (Spawn objects in the environment at specified position)
- [communicator.spawn_agent](simworld/communicator/communicator.py#L603) (Spawn agents like humanoids or robots in the environment)
- [communicator.generate_world](simworld/communicator/communicator.py#L812) (Generate procedural city world from configuration)
- [communicator.clear_env](simworld/communicator/communicator.py#L880) (Clear all objects from the environment)

<a id="make-your-simworld"></a>
## 🛠️ Make Your SimWorld

Bring your own Unreal Engine environments, assets, and agent models into SimWorld. This lets you add new maps, objects, and characters beyond the built-in library. For example, you can turn almost any idea into a playable world, such as a rainy campus, a night market, or a sci-fi city, and then drop agents into it to explore, interact, and learn. To import your content into SimWorld, package it as a custom `.pak` file. See full instructions in [Make Your Own Pak Files](https://simworld.readthedocs.io/en/latest/customization/make_your_own_pak.html).

## 🔮 Next Steps

The SimWorld framework is under active development. Future releases will include:

- [x] **Plugin System**: Support for importing user-defined custom environments and agents to extend SimWorld's capabilities ([doc](https://simworld.readthedocs.io/en/latest/customization/make_your_own_pak.html)).
- [ ] **Comprehensive Agent Framework**: A unified training and evaluation pipeline for autonomous agents.
- [ ] **Code Generation for Scenes**: AI-powered coding agents capable of generating diverse simulation scenarios programmatically.
- [ ] **Interactive Layout Editor**: Web-based interface for real-time city layout visualization and editing.

## 🤝 Contributing

We welcome contributions from the community! Whether you want to report bugs, suggest features, or submit code improvements, your input is valuable. Please check out our [Contributing Guidelines](CONTRIBUTING.md) for details on how to get started.

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=SimWorld-AI/SimWorld&type=date&legend=bottom-right)](https://www.star-history.com/#SimWorld-AI/SimWorld&type=date&legend=bottom-right)
