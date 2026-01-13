Installation
============

This page shows how to download and install the packaged version of SimWorld. The package includes the executable file of the SimWorld server and the Python client library.

Before you begin
-----------------

The following device requirements should be fulfilled before installing SimWorld:

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Category
     - Minimum
     - Recommended
   * - OS
     - Windows / Linux
     - Windows / Linux
   * - GPU
     - ≥ 6 GB VRAM (dedicated GPU recommended)
     - ≥ 8 GB VRAM (dedicated GPU strongly recommended)
   * - Memory (RAM)
     - 32 GB
     - 32 GB+
   * - Disk Space
     - 50 GB (Base)
     - 200 GB+ (Additional Environments)

.. warning::

   1. Python: Python 3.10 or later is required.
   2. Network: A stable internet connection and available TCP port (9000 by default) are required.
   3. In our demo video, we use RTX 4090 with 24 GB VRAM for video recording, and hardware raytracing is enabled for enhanced visual fidelity.

Installation
------------

SimWorld Python Client Library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SimWorld Python Client Library contains code for SimWorld's agent and environment layer. Download the Python library from GitHub: `SimWorld Python Client Library <https://github.com/SimWorld-AI/SimWorld.git>`_

.. code-block:: bash

   git clone https://github.com/SimWorld-AI/SimWorld.git
   cd SimWorld

   # install simworld
   conda create -n simworld python=3.10
   conda activate simworld
   pip install -e .

Unreal Engine Backend
~~~~~~~~~~~~~~~~~~~~~

Download the SimWorld Unreal Engine backend executable from huggingface. Choose the version according to your OS and the edition you want to use. 

.. list-table::
   :header-rows: 1
   :widths: 15 15 30 25 15

   * - Platform
     - Package
     - Scenes/Maps Included
     - Download
     - Notes
   * - Windows
     - Base
     - Empty map for procedural generation
     - `Download for Windows <https://huggingface.co/datasets/SimWorld-AI/SimWorld/resolve/main/Base/Windows.zip>`_
     - Full agent features; smaller download.
   * - Linux
     - Base
     - Empty map for procedural generation
     - `Download for Linux <https://huggingface.co/datasets/SimWorld-AI/SimWorld/resolve/main/Base/Linux.zip>`_
     - Full agent features; smaller download.

You can also download the Additional Environments Paks from this huggingface `link <https://huggingface.co/datasets/SimWorld-AI/SimWorld/tree/main/AdditionEnvironmentPaks>`_. The usage of the Additional Environments Paks can be found on the :doc:`additional_environments` page.

.. note::

   If you only need core functionality for development or testing, use **Base**. If you want more scenes, see :doc:`additional_environments` page to setup addition environments.