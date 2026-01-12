# Installation

This page shows how to download and install the packaged version of SimWorld. The package includes the executable file of the SimWorld server and the Python client library.

## Before you begin
The following device requirements should be fulfilled before installing SimWorld:

| Category | Minimum | Recommended |
|---|---|---|
| OS | Windows / Linux | Windows / Linux |
| GPU | ≥ 6 GB VRAM (dedicated GPU recommended) | ≥ 8 GB VRAM (dedicated GPU strongly recommended) |
| Memory (RAM) | 32 GB | 32 GB+ |
| Disk Space | 50 GB (Base) | 200 GB+ (Additional Environments) |


.. warning::

   1. Python: Python 3.10 or later is required.
   2. Network: A stable internet connection and available TCP port (9000 by default) are required.
   3. In our demo video, we use RTX 4090 with 24 GB VRAM for video recording, and hardware raytracing is enabled for enhanced visual fidelity.

## Installation
### SimWorld Python Client Library
The SimWorld Python Client Library contains code for SimWorld's agent and environment layer. Download the Python library from GitHub:

.. tip::

   [SimWorld Python Client Library](https://github.com/SimWorld-AI/SimWorld.git)

```bash
git clone https://github.com/SimWorld-AI/SimWorld.git
cd SimWorld

# install simworld
conda create -n simworld python=3.10
conda activate simworld
pip install -e .
```

### Unreal Engine Backend
Download the SimWorld Unreal Engine backend executable from AWS S3. Choose the version according to your OS and the edition you want to use. The usage of the Additional Environments version can be found on the [Additional Environments](../getting_started/additional_environments) page.

| Platform | Package | Scenes/Maps Included | Download | Notes |
| --- | --- | --- | --- | --- |
| Windows | Base | Empty map for procedural generation | [Download (Base)](https://huggingface.co/SimWorld-AI/SimWorld/resolve/main/Windows.zip) | Full agent features; smaller download. |
| Linux | Base | Empty map for procedural generation | [Download (Base)](https://huggingface.co/SimWorld-AI/SimWorld/resolve/main/Linux.zip) | Full agent features; smaller download. |

.. note::

   If you only need core functionality for development or testing, use **Base**. If you want richer demonstrations and more scenes, see [Additional Environments](../getting_started/additional_environments) page to setup addition environments.
