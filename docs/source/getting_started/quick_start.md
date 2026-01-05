# Quick Start

This page shows how to download and install the packaged version of SimWorld. The package includes the executable file of SimWorld server and the Python client library.

## Before you begin
The following requirements should be fulfilled before installing SimWorld:

+ System requirements. SimWorld is built for Windows and Linux systems.
+ An adequate GPU. SimWorld aims for realistic simulations, so the server needs at least a 6 GB GPU although we would recommend 8 GB. A dedicated GPU is highly recommended for machine learning.
+ Memory. A 32 GB memory or above is recommended.
+ Disk space. SimWorld will use about 50 GB of space.
+ Python. SimWorld supports Python 3.10 or higher.
+ Two TCP ports and good internet connection. 9000 and 9001 by default. Make sure that these ports are not blocked by firewalls or any other applications.

## Installation
### Agent and Environment Client
Download the Python library from GitHub:

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
Download the SimWorld Unreal Engine backend executable from S3, choose the version according to your OS and the edition you want to use, the usage of the additional environments version can be shown in the [Additional Environments](../getting_started/addisional_envrionments) page.

| OS | Edition | Download |
| --- | --- | --- |
| Windows | Base | [SimWorld Windows 64-bit Unreal Engine Backend (v0.1.0) - base version](https://simworld-release.s3.us-east-1.amazonaws.com/SimWorld-Win64-v0_1_0-Foundation.zip) |
| Windows | Additional environments | [SimWorld Windows 64-bit Unreal Engine Backend (v0.1.0) - additional environments version](https://simworld-release.s3.us-east-1.amazonaws.com/SimWorld-Win64-v0_1_0-100Maps.zip) |
| Linux | Base | [SimWorld Linux 64-bit Unreal Engine Backend (v0.1.0) - base version](https://simworld-release.s3.us-east-1.amazonaws.com/SimWorld-Linux-v0_1_0-Foundation.zip) |
| Linux | Additional environments | [SimWorld Linux 64-bit Unreal Engine Backend (v0.1.0) - additional environments version](https://simworld-release.s3.us-east-1.amazonaws.com/SimWorld-Linux-v0_1_0-100Maps.zip) |
