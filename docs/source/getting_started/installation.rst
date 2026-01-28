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
   2. We use port 9000 by default for communication between the SimWorld server and the Python client. Please ensure that this port is available when running SimWorld.
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

First, download and extract the **Base** UE server package for your OS. The Base package includes 2 lightweight lightweight city scenes and 1 empty map for quickly testing SimWorld's core features, including core agent interaction and procedural city generation. See :doc:`base_environments` for details.

* **Base (Required)**

  * **Windows:** `Download <https://huggingface.co/datasets/SimWorld-AI/SimWorld/resolve/main/Base/Windows.zip>`_
  * **Linux:** `Download <https://huggingface.co/datasets/SimWorld-AI/SimWorld/resolve/main/Base/Linux.zip>`_

If you want more pre-built scenes for demos and diverse scenarios, you can optionally install **Additional Environments (100+ Maps)**. This is an add-on map pack that extends the Base installation. Download the maps you need and copy the ``.pak`` files into the Base server folder at: ``SimWorld/Content/Paks/``.

* **Additional Environments (Optional, 100+ Maps)**

  * **Windows:** `Download <https://huggingface.co/datasets/SimWorld-AI/SimWorld/tree/main/AdditionEnvironmentPaks/Windows>`_
  * **Linux:** `Download <https://huggingface.co/datasets/SimWorld-AI/SimWorld/tree/main/AdditionEnvironmentPaks/Linux>`_

The Additional Environments package is organized as separate ``.pak`` files, so you can download only the maps you need. Please check the :doc:`additional_environments` documentation for usage instructions, including how to load specific maps and what each ``.pak`` contains.