# UnrealCV+

## Overview
<!-- ```{image} ../assets/communicator.png
:width: 800px
:align: center
:alt: Communicator Architecture
``` -->
**UnrealCV+** is a communication module that bridges the Unreal Engine backend and the Environment layer, enabling efficient and reliable interaction between them over a TCP connection. Built upon the original [UnrealCV](https://unrealcv.org/) framework, UnrealCV+ extends its capabilities to support large-scale, real-time embodied AI simulations. Implemented in both Python and C++, it provides flexible data exchange and fine-grained control over the simulation process.

UnrealCV+ introduces a custom command set designed for agent-based tasks, including scene control, actor manipulation, and data querying. For example, users or the environment layer can send commands such as: "spawn actors at locations", "get position of a pedestrian" and "execute action of a robot"

During each simulation loop, the Environment layer manages the logical progression of tasks, while the Unreal Engine continuously returns updated physical states and visual observations. All data and commands are transmitted through UnrealCV+, forming a decoupled architecture that separates logic computation from rendering—greatly improving flexibility, scalability, and modularity.

UnrealCV+ is open-sourced (both UE and Python), allowing users to customize and build their own simulation environments directly within the Unreal Engine Editor using personal or third-party assets.

## Communicator
UnrealCV+ is realized through the `Communicator` and `UnrealCV` classes in Python. The `Communicator` class serves as the primary interface between Python and Unreal Engine (UE), managing all interactions between the two. It holds an `unrealcv` attribute—an instance of the `UnrealCV` class—which is responsible for establishing and maintaining the underlying TCP connection.

```python
class Communicator:
    def __init__(self, unrealcv: UnrealCV = None):
        """Initialize the communicator.

        Args:
            unrealcv: UnrealCV instance for communication with Unreal Engine.
        """
        self.unrealcv = unrealcv
        ...

class UnrealCV:
    def __init__(self, port=9000, ip='127.0.0.1', resolution=(640, 480)):
        """Initialize the UnrealCV client.

        Args:
            port: Connection port, defaults to 9000.
            ip: Connection IP address, defaults to 127.0.0.1.
            resolution: Resolution, defaults to (320, 240).
        """
        self.ip = ip
        # Build a client to connect to the environment
        self.client = unrealcv.Client((ip, port))
        self.client.connect()
        self.resolution = resolution
        ...
```


## Using Communicator
All communication between Python and UE—such as rendering the scene, simulating traffic, or interacting with agents—is handled through the Communicator. Below are some basic use cases, including how to generate a city in UE, spawn objects, and clean the environment. For complete functionality, refer to the [Python API](../resources/modules.md).

```python
# Instantiate unrealcv and communicator first
ucv = UnrealCV()
communicator = Communicator(ucv)

# Render a city
communicator.generate_world('path/to/city_json', 'path/to/asset_database')

# Spawn objects
## Spawn static object (non-movable)
communicator.spawn_object(object_name, model_path, position, direction)
## Spawn an agent (controlled by LLM or rule-based logic)
communicator.spawn_agent(agent, model_path, type)  
## Spawn the UE Manager actor (required for agent physical state updates)  
communicator.spawn_ue_manager(ue_manager_path)  

# Clear the UE environment (optionally keeping roads)
communicator.clear_env(keep_roads=True)
```
