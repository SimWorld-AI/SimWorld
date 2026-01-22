Introduction
============

Overview
--------

**SimWorld** is an Unreal Engine 5-based simulator for creating rich, dynamic, and photorealistic environments to support embodied AI research. Unlike most existing simulators that focus on indoor or task-specific domains (e.g., household robotics or autonomous driving), SimWorld enables large-scale, open-ended outdoor simulation with realistic physical and social dynamics.

Through its user-friendly Python API and extensive 3D asset library, users can procedurally generate diverse city layouts or load high-quality, pre-defined environments sourced from the Unreal Marketplace. This flexibility allows researchers to easily design experiments ranging from navigation and interaction to multi-agent collaboration.

SimWorld also integrates seamlessly with large language models (LLMs) and vision-language models (VLMs), enabling agents to perceive, reason, and act in complex, dynamic worlds. With SimWorld, you can explore embodied intelligence at scale—combining procedural generation, realistic simulation, and language-driven control in one unified platform.

Architecture
------------

.. important::

   SimWorld employs a three-tier hierarchical architecture that separates the high-performance *Unreal Engine Backend* from two Python-side layers: the *Environment* layer and the *Agent* layer.

.. image:: ../assets/Arch.png
   :width: 800px
   :align: center
   :alt: SimWorld Architecture

SimWorld employs a three-tier hierarchical architecture that separates the high-performance *Unreal Engine Backend* from two Python-side layers: the *Environment* layer and the *Agent* layer. Python and Unreal Engine are connected through the *UnrealCV+* communication module, which enables seamless interaction and data exchange between Unreal Engine and Python components.

At its core, the *Unreal Engine Backend* provides high-fidelity scenes, assets, and physics, forming the foundation for realistic simulation. Built upon it, the *Environment* layer serves as an intermediary that abstracts low-level rendering and physics into structured representations, supporting procedural city generation, traffic simulation, and a Gym-like interface for agent interaction via *UnrealCV+*. On top of this, the *Agent* layer integrates LLM/VLM agents capable of interpreting multimodal observations from the environment, reasoning about goals, and issuing actions that are executed through the environment's connection to the Unreal backend. Together, these components form a closed perception–planning–action loop, enabling intelligent agents to interact, learn, and adapt in rich, dynamic worlds.

UE Server Packages
------------------

First, download and extract the **Base** UE server package for your OS. The Base package includes a lightweight city scene for quickly testing SimWorld’s core features, including core agent interaction and procedural city generation.

* **Base (Required)**

  * **Windows:** `Download <https://huggingface.co/datasets/SimWorld-AI/SimWorld/resolve/main/Base/Windows.zip>`_
  * **Linux:** `Download <https://huggingface.co/datasets/SimWorld-AI/SimWorld/resolve/main/Base/Linux.zip>`_

If you want more pre-built scenes for demos and diverse scenarios, you can optionally install **Additional Environments (100+ Maps)**. This is an add-on map pack that extends the Base installation. Download the maps you need and copy the ``.pak`` files into the Base server folder at: ``SimWorld/Content/Paks/``.

* **Additional Environments (Optional, 100+ Maps)**

  * **Windows:** `Download <https://huggingface.co/datasets/SimWorld-AI/SimWorld/tree/main/AdditionEnvironmentPaks/Windows>`_
  * **Linux:** `Download <https://huggingface.co/datasets/SimWorld-AI/SimWorld/tree/main/AdditionEnvironmentPaks/Linux>`_

The Additional Environments package is organized as separate ``.pak`` files, so you can download only the maps you need. Please check the :doc:`additional_environments` documentation for usage instructions, including how to load specific maps and what each ``.pak`` contains.


Next Steps
----------

The SimWorld framework is under active development. Future releases will include:

.. list-table::
   :widths: 5 95
   :class: tight-table

   * - ☑
     - **Plugin System:** Support for importing user-defined custom environments and agents to extend SimWorld's capabilities.
   * - ☐
     - **Comprehensive Agent Framework:** A unified training and evaluation pipeline for autonomous agents.
   * - ☐
     - **Code Generation for Scenes:** AI-powered coding agents capable of generating diverse simulation scenarios programmatically.
   * - ☐
     - **Interactive Layout Editor:** Web-based interface for real-time city layout visualization and editing.