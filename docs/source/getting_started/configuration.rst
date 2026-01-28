Configuration Reference
========================

SimWorld uses a YAML configuration file to control global simulator settings and module behaviors. This page provides a comprehensive reference for all configuration parameters in ``default.yaml``.

Overview
--------

The configuration file is organized into several main sections.

* ``simworld``: Global simulator settings
* ``citygen``: Procedural city generation parameters
* ``assets_rp``: Asset retrieval and placement settings
* ``traffic``: Traffic simulation configuration
* ``map``: Map-related settings
* ``user``: User agent configuration
* ``scooter``: Scooter agent settings

Quick guidance
--------------

* Core knobs: ``simworld`` is the primary global block most users tweak (e.g., seed, dt, UE manager path). Start here.
* Advanced blocks: ``citygen``, ``assets_rp``, ``traffic``, ``map``, ``user``, and ``scooter`` expose detailed behaviors. In most cases you can keep their defaults unchanged unless you need specific generation or simulation customization.

Global Settings (simworld)
---------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Parameter
     - Type
     - Description
   * - ``seed``
     - int
     - Random seed for reproducibility. Default: ``42``
   * - ``dt``
     - float
     - Time step (delta time) for simulation in seconds. Default: ``0.1``
   * - ``ue_manager_path``
     - str
     - Unreal Engine blueprint path to the UE Manager class. Default: ``"/Game/TrafficSystem/UE_Manager.UE_Manager_C"``

City Generation (citygen)
--------------------------

City generation parameters control procedural city creation, including roads, buildings, and city elements.

Input/Output Paths
~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Parameter
     - Type
     - Description
   * - ``input_layout``
     - bool
     - Whether to use an input layout file. Default: ``false``
   * - ``input_roads``
     - str
     - Path to input roads JSON file. Use ``"<path to your roads.json>"`` as placeholder
   * - ``input_bounding_boxes``
     - str
     - Path to bounding boxes JSON file. Default: ``"bounding_boxes.json"``
   * - ``output_dir``
     - str
     - Directory for output files. Default: ``"output"``
   * - ``world_json``
     - str
     - Name of the generated world JSON file. Default: ``"progen_world.json"``
   * - ``ue_asset_path``
     - str
     - Path to UE assets JSON file. Default: ``"ue_assets.json"``

Road Generation
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Parameter
     - Type
     - Description
   * - ``segment_length``
     - int
     - Length of each road segment in Unreal units. Default: ``200``
   * - ``segment_count_limit``
     - int
     - Maximum number of segments per road. Default: ``10``
   * - ``road_snap_distance``
     - int
     - Distance threshold for snapping roads together. Default: ``90``
   * - ``ignore_conflicts``
     - bool
     - Whether to ignore road conflicts during generation. Default: ``false``
   * - ``only_highway``
     - bool
     - Generate only highways. Default: ``false``
   * - ``two_segment_init``
     - bool
     - Initialize roads with two segments. Default: ``true``
   * - ``time_delay_between_segments``
     - float
     - Time delay between generating road segments in seconds. Default: ``0.001``
   * - ``minimum_intersection_deviation``
     - int
     - Minimum angle deviation for intersections in degrees. Default: ``30``

Building Placement
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Parameter
     - Type
     - Description
   * - ``building_road_distance``
     - int
     - Minimum distance between buildings and roads. Default: ``25``
   * - ``building_intersection_distance``
     - int
     - Minimum distance between buildings and intersections. Default: ``0``
   * - ``building_building_distance``
     - int
     - Minimum distance between buildings. Default: ``0``
   * - ``building_side_distance``
     - int
     - Distance from building to road side. Default: ``27``

Element Generation
~~~~~~~~~~~~~~~~~~

City elements include parking spaces, furniture, and trees.

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Parameter
     - Type
     - Description
   * - ``generation``
     - bool
     - Enable element generation. Default: ``false``
   * - ``generation_thread_number``
     - int
     - Number of threads for parallel element generation. Default: ``16``
   * - ``element_building_distance``
     - int
     - Minimum distance between elements and buildings. Default: ``8``
   * - ``element_element_distance``
     - int
     - Minimum distance between elements. Default: ``10``
   * - ``add_building_attempts``
     - int
     - Number of attempts to place buildings. Default: ``10``

Element Offsets
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Parameter
     - Type
     - Description
   * - ``parking_offset``
     - int
     - Offset distance for parking spaces. Default: ``10``
   * - ``furniture_offset``
     - int
     - Offset distance for furniture placement. Default: ``12``
   * - ``tree_offset``
     - int
     - Offset distance for tree placement. Default: ``23``

Element Density
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Parameter
     - Type
     - Description
   * - ``parking_density``
     - float
     - Density of parking spaces (0.0 to 1.0). Default: ``0.05``
   * - ``furniture_density``
     - float
     - Density of furniture (0.0 to 1.0). Default: ``0.05``
   * - ``tree_density``
     - float
     - Density of trees (0.0 to 1.0). Default: ``0.1``

Quadtree Settings
~~~~~~~~~~~~~~~~~~

Quadtree is used for spatial indexing and collision detection.

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Parameter
     - Type
     - Description
   * - ``max_levels``
     - int
     - Maximum quadtree depth levels. Default: ``10``
   * - ``max_objects``
     - int
     - Maximum objects per quadtree node. Default: ``10``
   * - ``bounds.x``
     - int
     - X coordinate of quadtree bounds origin. Default: ``-2000``
   * - ``bounds.y``
     - int
     - Y coordinate of quadtree bounds origin. Default: ``-2000``
   * - ``bounds.width``
     - int
     - Width of quadtree bounds. Default: ``4000``
   * - ``bounds.height``
     - int
     - Height of quadtree bounds. Default: ``4000``

Route Generation
~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Parameter
     - Type
     - Description
   * - ``generation``
     - bool
     - Enable route generation. Default: ``false``
   * - ``number``
     - int
     - Number of routes to generate. Default: ``2``
   * - ``min_points_per_route``
     - int
     - Minimum waypoints per route. Default: ``2``
   * - ``max_points_per_route``
     - int
     - Maximum waypoints per route. Default: ``5``

Asset Retrieval and Placement (assets_rp)
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Parameter
     - Type
     - Description
   * - ``input_description_map``
     - str
     - Path to description map JSON file. Default: ``"description_map.json"``
   * - ``input_sample_dataset``
     - str
     - Path to sample dataset directory. Default: ``"asset_images"``
   * - ``output_dir``
     - str
     - Output directory for retrieved assets. Default: ``"output_rp"``
   * - ``env_description_retrieval_model``
     - str
     - Model name for environment description retrieval. Default: ``"paraphrase-MiniLM-L6-v2"``
   * - ``assets_retrieval_model``
     - str
     - Model name for asset retrieval. Default: ``"openai/clip-vit-large-patch14-336"``
   * - ``progen_world_path``
     - str
     - Path to generated world JSON file. Default: ``"progen_world.json"``

Traffic Simulation (traffic)
-----------------------------

General Traffic Settings
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Parameter
     - Type
     - Description
   * - ``num_vehicles``
     - int
     - Number of vehicles in simulation. Default: ``10``
   * - ``num_pedestrians``
     - int
     - Number of pedestrians in simulation. Default: ``10``
   * - ``map_path``
     - str
     - Path to roads JSON file. Default: ``"roads.json"``
   * - ``distance_between_objects``
     - int
     - Minimum distance between traffic objects in Unreal units. Default: ``400``
   * - ``detection_angle``
     - int
     - Detection angle for traffic objects in degrees. Default: ``40``
   * - ``gap_between_waypoints``
     - int
     - Distance between waypoints in Unreal units. Default: ``800``
   * - ``num_lanes``
     - int
     - Number of lanes per road. Default: ``1``
   * - ``lane_offset``
     - int
     - Offset between lanes in Unreal units. Default: ``300``
   * - ``intersection_offset``
     - int
     - Offset from intersection center in Unreal units. Default: ``3000``
   * - ``sidewalk_offset``
     - int
     - Offset for sidewalk placement in Unreal units. Default: ``1700``
   * - ``crosswalk_offset``
     - int
     - Offset for crosswalk placement in Unreal units. Default: ``1700``
   * - ``steering_point_num``
     - int
     - Number of steering points for path planning. Default: ``12``

Pedestrian Settings
~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Parameter
     - Type
     - Description
   * - ``max_speed``
     - int
     - Maximum pedestrian speed in Unreal units per second. Default: ``200``
   * - ``min_speed``
     - int
     - Minimum pedestrian speed in Unreal units per second. Default: ``100``
   * - ``waypoint_distance_threshold``
     - int
     - Distance threshold for waypoint arrival in Unreal units. Default: ``200``
   * - ``model_path``
     - str
     - Unreal Engine blueprint path to pedestrian model. Default: ``"/Game/TrafficSystem/Pedestrian/Base_Pedestrian.Base_Pedestrian_C"``

Vehicle Settings
~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Parameter
     - Type
     - Description
   * - ``steering_pid.kp``
     - float
     - Proportional gain for steering PID controller. Default: ``0.15``
   * - ``steering_pid.ki``
     - float
     - Integral gain for steering PID controller. Default: ``0.005``
   * - ``steering_pid.kd``
     - float
     - Derivative gain for steering PID controller. Default: ``0.12``
   * - ``max_steering``
     - float
     - Maximum steering angle. Default: ``0.5``
   * - ``lane_deviation``
     - int
     - Maximum allowed lane deviation in Unreal units. Default: ``70``
   * - ``distance_to_end``
     - int
     - Distance threshold to route end in Unreal units. Default: ``400``
   * - ``model_file_path``
     - str
     - Path to vehicle types JSON file. Default: ``"vehicle_types.json"``

Traffic Signal Settings
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Parameter
     - Type
     - Description
   * - ``light_normal_offset``
     - int
     - Normal offset for traffic light placement in Unreal units. Default: ``-1400``
   * - ``light_radial_offset``
     - int
     - Radial offset for traffic light placement in Unreal units. Default: ``1400``
   * - ``traffic_light_model_path``
     - str
     - Unreal Engine blueprint path to traffic light model. Default: ``"/Game/city_props/BP/props/street_light/BP_street_light.BP_street_light_C"``
   * - ``pedestrian_light_model_path``
     - str
     - Unreal Engine blueprint path to pedestrian light model. Default: ``"/Game/city_props/BP/props/street_light/BP_street_light_ped.BP_street_light_ped_C"``
   * - ``green_light_duration``
     - int
     - Duration of green light in seconds. Default: ``10``
   * - ``yellow_light_duration``
     - int
     - Duration of yellow light in seconds. Default: ``2``
   * - ``pedestrian_green_light_duration``
     - int
     - Duration of pedestrian green light in seconds. Default: ``30``

Map Settings (map)
------------------

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Parameter
     - Type
     - Description
   * - ``input_roads``
     - str
     - Path to input roads JSON file. Default: ``"roads.json"``

User Agent Settings (user)
---------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Parameter
     - Type
     - Description
   * - ``num_agents``
     - int
     - Number of user agents. Default: ``3``
   * - ``speed``
     - int
     - Agent movement speed in Unreal units per second. Default: ``200``
   * - ``a2a``
     - bool
     - Enable agent-to-agent communication. Default: ``true``
   * - ``rule_based``
     - bool
     - Use rule-based behavior. Default: ``true``
   * - ``waypoint_distance_threshold``
     - int
     - Distance threshold for waypoint arrival in Unreal units. Default: ``150``
   * - ``model_path``
     - str
     - Unreal Engine blueprint path to user agent model. Default: ``"/Game/TrafficSystem/Pedestrian/Base_User_Agent.Base_User_Agent_C"``
   * - ``num_threads``
     - int
     - Number of threads for agent processing. Default: ``20``
   * - ``llm_model_path``
     - str
     - LLM model identifier or path. Default: ``"gpt-4o-mini"``
   * - ``llm_url``
     - str/None
     - Custom LLM API URL. Set to ``None`` to use default provider. Default: ``None``
   * - ``llm_provider``
     - str
     - LLM provider name (e.g., "openai", "anthropic"). Default: ``"openai"``

Scooter Settings (scooter)
---------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Parameter
     - Type
     - Description
   * - ``model_path``
     - str
     - Unreal Engine blueprint path to scooter model. Default: ``"/Game/ScooterAssets/Blueprints/BP_Scooter_Pawn.BP_Scooter_Pawn_C"``

Creating Your Own Configuration
--------------------------------

To create a custom configuration:

1. Copy the example template:

   .. code-block:: bash

      cp config/example.yaml config/your_config.yaml

2. Modify the values in ``your_config.yaml`` according to your needs.

3. Load your configuration in Python:

   .. code-block:: python

      from simworld.config import Config
      config = Config('path/to/your_config')  # use absolute path here

.. note::

   The ``default.yaml`` file contains built-in defaults shipped with the package. We recommend **not editing** this file directly. Instead, create your own configuration file based on ``example.yaml``.
