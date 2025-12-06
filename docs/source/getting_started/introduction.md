# Introduction

## Overview
**SimWorld** is an Unreal Engine 5–based simulator for creating rich, dynamic, and photorealistic environments to support embodied AI research. Unlike most existing simulators that focus on indoor or task-specific domains (e.g., household robotics or autonomous driving), SimWorld enables large-scale, open-ended outdoor simulation with realistic physical and social dynamics.

Through its user-friendly Python API and extensive 3D asset library, users can procedurally generate diverse city layouts or load high-quality, pre-defined environments sourced from the Unreal Marketplace. This flexibility allows researchers to easily design experiments ranging from navigation and interaction to multi-agent collaboration.

SimWorld also integrates seamlessly with large language models (LLMs) and vision-language models (VLMs), enabling agents to perceive, reason, and act in complex, dynamic worlds. With SimWorld, you can explore embodied intelligence at scale—combining procedural generation, realistic simulation, and language-driven control in one unified platform.

## Architecture

```{image} ../assets/Arch.png
:width: 800px
:align: center
:alt: SimWorld Architecture
```

SimWorld employs a three-tier hierarchical architecture that separates the high-performance *Unreal Engine Backend* from two Python-side layers: the *Environment* layer and the *Agent* layer. This design is connected through the *UnrealCV+* communication module, which enables seamless interaction and data exchange between Unreal Engine and Python components.

At its core, the *Unreal Engine Backend* provides high-fidelity scenes, assets, and physics, forming the foundation for realistic simulation. Built upon it, the *Environment* layer serves as an intermediary that abstracts low-level rendering and physics into structured representations, supporting procedural city generation, traffic simulation, and a Gym-like interface for agent interaction via *UnrealCV+*. On top of this, the *Agent* layer integrates LLM/VLM agents capable of interpreting multimodal observations from the environment, reasoning about goals, and issuing actions that are executed through the environment’s connection to the Unreal backend. Together, these components form a closed perception–planning–action loop, enabling intelligent agents to interact, learn, and adapt in rich, dynamic worlds.


```{image} ../assets/architecture.png
:width: 800px
:align: center
:alt: SimWorld Server-Client Architecture
```

SimWorld adopts a robust and scalable client-server design that enables efficient simulation and agent control. The server component, built on Unreal Engine 5, serves as the simulation backbone, handling critical tasks such as sensor rendering, physical simulation and updates on the world-state.

The client component, implemented in Python, provides a flexible and developer-friendly interface for:
- Agent control logic and decision-making
- Seamless integration with LLM/VLM models
- Custom scenario configuration and management

