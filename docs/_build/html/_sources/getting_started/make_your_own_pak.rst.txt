Make Your Own Pak Files
=======================

You can create your own .pak files to extend the environment or agent library of SimWorld by following these steps:

.. note::

   - We use Windows for this tutorial, but the steps are similar for Linux.
   - If you are on Windows, you can use cross-compiling to build pak files for Linux by refering this document: `Unreal Engine Linux Cross-Compilation <https://dev.epicgames.com/documentation/en-us/unreal-engine/linux-development-requirements-for-unreal-engine?application_version=5.3#cross-compiletoolchain>`_.

1. Download the Unreal Editor
-----------------------------

Download the Unreal Editor from the `Epic Games Launcher <https://www.unrealengine.com/en-US/download>`_. The Latest version of SimWorld is using Unreal Engine 5.3.2, so make sure to install the same version.

.. image:: ../assets/MYO_1.png
   :width: 800px
   :align: center
   :alt: Epic Games Launcher
   :class: with-margin

2. Create a New Unreal Project
------------------------------

Launch the Unreal Engine and create a new project. Then name the project as ``SimWorld`` to match the SimWorld structure.

.. image:: ../assets/MYO_2.png
   :width: 800px
   :align: center
   :alt: Create New Project
   :class: with-margin

.. warning::

   Make sure your project has been named as ``SimWorld``, otherwise the pak file may not work properly.

3. Import Assets
----------------

.. tip:: Asset Organization

   Import your desired assets into the project. You can use assets from the Unreal Marketplace or your own custom assets. Make sure all assets are properly organized in **a same** folder under the ``Content`` directory.

.. image:: ../assets/MYO_3.png
   :width: 800px
   :align: center
   :alt: Import Assets
   :class: with-margin

4. Setup Chunk Package
-----------------------

Open project settings by navigating to ``Edit > Project Settings``. In the Project Settings window, go to the ``Packaging`` section and enable the ``Use Pak File`` option, **disenable** ``Use Io Store``, and enable ``Generate Chunks``.

.. image:: ../assets/MYO_4.png
   :width: 800px
   :align: center
   :alt: Package Settings
   :class: with-margin

Then, add a ``Data Asset`` at the directory where you imported your assets. Right-click in the Content Browser, select ``Miscellaneous > Data Asset``, and choose ``Primary Asset Label`` to create a new Data Asset.

.. image:: ../assets/MYO_5.png
   :width: 800px
   :align: center
   :alt: Create Data Asset
   :class: with-margin


5. Configure Chunk Settings
----------------------------

Open the created Data Asset and set the ``ChunkID``. And enable all options under ``Primary Asset Label`` to make sure all assets under this directory will be included in the pak file.

.. image:: ../assets/MYO_6.png
   :width: 800px
   :align: center
   :alt: Configure Chunk Settings
   :class: with-margin


.. important::

   The ``ChunkID`` should be unique and not conflict with existing chunks in SimWorld. You can refer to the :doc:`additional_environments` to avoid conflicts.


6. Build the Pak File
---------------------

Finally, package the project by navigating to ``Platforms > Windows > Package Project``. Choose a directory to save the packaged project. After packaging is complete, navigate to the saved directory and locate the ``.pak`` file in the ``<Path to your packaged project>/SimWorld/Content/Paks`` folder.

.. image:: ../assets/MYO_7.png
   :width: 800px
   :align: center
   :alt: Package Project
   :class: with-margin


7. Use the Pak File in SimWorld
-------------------------------

Copy the generated ``.pak`` file to the ``SimWorld/Content/Paks`` directory of your SimWorld installation. You can now load the new environment or assets in SimWorld by specifying the corresponding Map URI or asset path. Refer to the :doc:`additional_environments` for loading instructions.