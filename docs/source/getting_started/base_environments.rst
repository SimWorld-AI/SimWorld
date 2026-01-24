Base Environments
=================

There are 3 base environments provided with SimWorld base package that can be start with. (See :doc:`installation` for download links)

.. list-table::
    :widths: 20 40 40
    
    * - Map Path
      - Description
      - Notes
    * - ``/Game/Maps/demo_1.umap``
      - A lightweight urban city environment with basic buildings, roads.
      - Default map loaded when starting the SimWorld binary without specifying a map.
    * - ``/Game/Maps/demo_2.umap``
      -  A lightweight urban city environment with basic buildings, roads.
      -  Similar to demo_1 but with different layout.
    * - ``/Game/Maps/empty.umap``
      - An empty environment with just a ground plane and sky.
      - Useful for testing :doc:`../components/citygen`.
  
Usage
-----

CLI
~~~

If you run SimWorld on a server, to load and use these additional environments you can refer to the `Unreal Engine Official Documentation <https://dev.epicgames.com/documentation/en-us/unreal-engine/command-line-arguments-in-unreal-engine>`_ to specify the desired Map URI when launching the unreal engine backend. 

.. seealso::

   For more details on command line arguments, see the `Unreal Engine Official Documentation <https://dev.epicgames.com/documentation/en-us/unreal-engine/command-line-arguments-in-unreal-engine>`_

For example, run the following command from the extracted UE server directory:

on Windows:

.. code-block:: bash

   ./SimWorld.exe /Game/Maps/demo_2.umap

or on Linux:

.. code-block:: bash

   ./SimWorld.sh /Game/Maps/demo_2.umap

GUI
~~~

If you run SimWorld on a machine with a GUI, you can switch the map after launching the SimWorld Unreal Engine backend by using the console command in the console window:

1. Press ``~`` to open the console window
2. Type ``open /Game/Maps/demo_2.umap`` and press enter
