Next Steps Roadmap
===================

This page provides more details on several key directions on SimWorld's roadmap.
If you're interested in collaborating on any item below, please reach out to the corresponding contact listed for that project.

.. contents::
   :local:
   :depth: 1


.. _next-steps-comprehensive-agent-framework:

Comprehensive Agent Framework
-----------------------------

We plan to build a **general, modular agent framework** for autonomous agents in SimWorld, including:

- **Standardized agent modules** (perception, memory, reasoning, and learning) that can be flexibly composed (e.g., dynamic cheat sheets, CoT, reflection)
- **Gym-compatible interfaces** for RL training across a wide range of embodied tasks
- **Systematic ablations across environments** to understand what actually matters for success in long-horizon embodied tasks

If you're interested in contributing designs or use cases for this framework, please reach out to **jic182@ucsd.edu**.


.. _next-steps-nl-to-ue-actions:

Arbitrary Natural Language → UE Actions
---------------------------------------

SimWorld already exposes a rich set of low-level Unreal Engine actions (e.g., move, rotate, interact, pick up).
The next step is to support **mapping free-form natural language instructions to executable UE actions/tools**, for example:

- "Walk to the coffee shop on the left, then sit down at the table by the window."
- "Spawn ten pedestrians crossing the main street and record a 20-second video."

This involves:

- Designing an extensible **action schema / tool specification** for UE actions
- Training / prompting llm local planners that ground language into these tools
- Providing debugging and visualization tools for action traces

If you are working on language-to-action or tool-use agents and would like to build on SimWorld, please contact **lingjun@ucsd.edu**.


.. _next-steps-rl-training-pipeline:

RL Training Pipeline for SimWorld
--------------------

We plan to provide a **unified RL training pipeline** for diverse embodied tasks (e.g., DeliveryBench) in SimWorld, including:

- Gym-like environment wrappers
- Standard observation and reward interfaces for embodied tasks
- Reference training scripts (e.g., PPO, SAC, multi-agent RL)

This will make it straightforward to run **large-scale RL experiments** across diverse embodied tasks, and to derive insights that can guide the design of new RL algorithms.

If you are interested in RL research and exploration in embodied simulation settings, please reach out at **lingjun@ucsd.edu**.


.. _next-steps-city-scale-multi-agent:

City-Scale Multi-Agent Simulation
---------------------------------

One of SimWorld's long-term goals is to support **city-scale multi-agent simulation** with 1K+ concurrent agents in the same city,
covering pedestrians, vehicles, service robots, and other interactive entities.

Key directions include:

- Scalable simulation backends and load balancing across machines
- Rich social and physical interaction patterns between agents
- Tools for logging, visualization, and analysis of large-scale behaviors

This direction is especially relevant for research on **emergent behavior, social dynamics, and large-scale coordination**.
If you are interested in pushing city-scale simulations or have industrial use cases, please contact **jir015@ucsd.edu**.

