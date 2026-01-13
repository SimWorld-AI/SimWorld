Additional Environments
========================

The additional environments are packaged as .pak files which include over 100 pre-defined scenes sourced from the Unreal Marketplace. These environments cover a wide range of settings, including urban areas, industrial zones, natural landscapes, and interior spaces. In addition, you can make your own .pak files to extend the environment or agent library of SimWorld by following the :doc:`make_your_own_pak` guide.

Download and Installation
-------------------------

Download
~~~~~~~~

To use the additional environments, download the environments paks as needed from this huggingface `link <https://huggingface.co/datasets/SimWorld-AI/SimWorld/tree/main/AdditionEnvironmentPaks>`_.

.. important::

   You can refer to ``Predefined Environments List`` table at the end of this page for ChunkID and Asset Library information.

Installation
~~~~~~~~~~~~

After downloading the pak files, place them in the ``<SimWorld_Path>/SimWorld/Content/Paks/``, then start the ``SimWorld.exe`` or ``SimWorld.sh`` to load the additional environments.

Usage
-----

CLI
~~~

If you run SimWorld on a server, to load and use these additional environments you can refer to the `Unreal Engine Official Documentation <https://dev.epicgames.com/documentation/en-us/unreal-engine/command-line-arguments-in-unreal-engine>`_ to specify the desired Map URI when launching the unreal engine backend. 

.. seealso::

   For more details on command line arguments, see the `Unreal Engine Official Documentation <https://dev.epicgames.com/documentation/en-us/unreal-engine/command-line-arguments-in-unreal-engine>`_

For example:

on Windows:

.. code-block:: bash

   ./gym_citynav.exe /Game/TokyoStylizedEnvironment/Maps/Tokyo.umap

or on Linux:

.. code-block:: bash

   ./gym_citynav.sh /Game/TokyoStylizedEnvironment/Maps/Tokyo.umap

GUI
~~~

If you run SimWorld on a machine with a GUI, you can switch the map after launching the SimWorld Unreal Engine backend by using the console command in the console window:

1. Press ``~`` to open the console window
2. Type ``open /Game/TokyoStylizedEnvironment/Maps/Tokyo.umap`` and press enter

Predefined Environments List
----------------------------

The following table lists the scenes and their corresponding Map URIs included in the additional environments version of SimWorld:

.. list-table::
   :header-rows: 1
   :widths: 10 45 45

   * - ChunkID
     - Asset Library
     - Map URI
   * - 2001
     - QA Modular Parking
     - ``/Game/QA_ModularParking/Maps/Map_demonstration.umap``
   * - 2002
     - University Classroom Interior Environment / School Room
     - ``/Game/UNIVERSITY_CLASSROOM/Levels/Showcase.umap``
   * - 2003
     - Chinese Water Town Ver.1
     - ``/Game/ChineseWaterTown/Ver1/Map/DemoMap.umap``
   * - 2004
     - Venice – Fast Building
     - ``/Game/Venice_fast_building/Maps/Showcase.umap``
   * - 2005
     - Low Poly Medieval Interior and Constructions
     - ``/Game/LowPolyMedievalConstructions/Maps/Map_1.umap``
   * - 2005
     - Low Poly Medieval Interior and Constructions
     - ``/Game/LowPolyMedievalConstructions/Maps/Map_2.umap``
   * - 2005
     - Low Poly Medieval Interior and Constructions
     - ``/Game/LowPolyMedievalConstructions/Maps/Map_3.umap``
   * - 2005
     - Low Poly Medieval Interior and Constructions
     - ``/Game/LowPolyMedievalConstructions/Maps/Map_8.umap``
   * - 2005
     - Low Poly Medieval Interior and Constructions
     - ``/Game/LowPolyMedievalConstructions/Maps/Map_9.umap``
   * - 2005
     - Low Poly Medieval Interior and Constructions
     - ``/Game/LowPolyMedievalConstructions/Maps/Map_4_Top-Down.umap``
   * - 2005
     - Low Poly Medieval Interior and Constructions
     - ``/Game/LowPolyMedievalConstructions/Maps/Map_5_Top-Down.umap``
   * - 2005
     - Low Poly Medieval Interior and Constructions
     - ``/Game/LowPolyMedievalConstructions/Maps/Map_6_Top-Down.umap``
   * - 2005
     - Low Poly Medieval Interior and Constructions
     - ``/Game/LowPolyMedievalConstructions/Maps/Map_7_Top-Down.umap``
   * - 2006
     - Atmospheric Modular Underground Car Park & Hallways
     - ``/Game/ParkingGarage/Maps/UndergroundParking.umap``
   * - 2007
     - Tokyo Stylized Environment
     - ``/Game/TokyoStylizedEnvironment/Maps/Tokyo.umap``
   * - 2008
     - Lighthouse Island – High Quality Environment
     - ``/Game/Lighthouse_Island/Levels/Lighthouse_Demo_00.umap``
   * - 2009
     - Rocket Launch Command Center
     - ``/Game/Nimikko_CommandCenter/Scenes/CommandCenter.umap``
   * - 2010
     - Desert Ruins
     - ``/Game/desert_ruins/maps/Showcase.umap``
   * - 2011
     - Wild West City
     - ``/Game/Wild_West/Maps/WildWest.umap``
   * - 2012
     - Euro Champions Football Stadium
     - ``/Game/ErikStadium/Maps/Stadium.umap``
   * - 2013
     - Next Gen Modular Victorian Neoclassical City
     - ``/Game/ModularVictorianCity/Maps/Demo_Map.umap``
   * - 2014
     - Modular Gothic / Fantasy Environment
     - ``/Game/ModularGothicFantasyEnvironment/Maps/DemoMapDay.umap``
   * - 2014
     - Modular Gothic / Fantasy Environment
     - ``/Game/ModularGothicFantasyEnvironment/Maps/DemoMapNight.umap``
   * - 2015
     - Bunker
     - ``/Game/Bunker/Maps/demonstration_BUNKER.umap``
   * - 2016
     - Fantasy Medieval Castle Kit
     - ``/Game/CastleRiver/Maps/Demonstration.umap``
   * - 2017
     - Roof – City Pack
     - ``/Game/RoofProps/Scenes/Demo_Roof.umap``
   * - 2018
     - Fantasy Cave Environment Set
     - ``/Game/Cave/Maps/Demonstration.umap``
   * - 2019
     - Modular Temple Plaza 4K PBR
     - ``/Game/ModularTemplePlaza/Maps/ConceptMap.umap``
   * - 2020
     - Ancient Ruins
     - ``/Game/AnchientRuins/Maps/AncientRuins.umap``
   * - 2021
     - Racing Track Winter Landscape
     - ``/Game/racing_track/map/racing_track.umap``
   * - 2022
     - Ultimate Farming
     - ``/Game/UltimateFarming/Maps/TinyFields.umap``
   * - 2023
     - Hospital Inside
     - ``/Game/hospital/map/demo.umap``
   * - 2024
     - Modular Industrial Area
     - ``/Game/IndustrialArea/Maps/IndustrialArea.umap``
   * - 2025
     - Greek Island
     - ``/Game/Greek_island/Level/L_greek_island.umap``
   * - 2026
     - Supermarket
     - ``/Game/MMSupermarket/Maps/Supermarket_Map.umap``
   * - 2027
     - QA Holding Cells
     - ``/Game/QA_HoldingCells/Maps/QA_Holding_Cells_A.umap``
   * - 2027
     - QA Holding Cells
     - ``/Game/QA_HoldingCells/Maps/QA_Holding_Cells_B.umap``
   * - 2028
     - Victorian Train Station & Railroad
     - ``/Game/TrainStation/Maps/Demonstration.umap``
   * - 2028
     - Modular Urban City Asset Megapack
     - ``/Game/TrainStation/Maps/TrainStation_Optimised.umap``
   * - 2029
     - Old Factory
     - ``/Game/Old_Factory_01/Maps/Demoscene_01.umap``
   * - 2030
     - Container Yard Environment Set
     - ``/Game/ContainerYard/Maps/Demonstration.umap``
   * - 2030
     - Container Yard Environment Set
     - ``/Game/ContainerYard/Maps/Demonstration_Day.umap``
   * - 2031
     - Modular Courtyard 1.0
     - ``/Game/ModularCourtyard/Maps/SampleScene_overcast.umap``
   * - 2031
     - Modular Courtyard 1.0
     - ``/Game/ModularCourtyard/Maps/SampleScene_sanny.umap``
   * - 2032
     - Brushify – Arctic Pack
     - ``/Game/Brushify/Maps/Arctic/Arctic.umap``
   * - 2033
     - Modular Medieval Environment
     - ``/Game/Medieval_Environment/Real_Landscape/Default/Maps/Default_Demo.umap``
   * - 2033
     - Modular Medieval Environment
     - ``/Game/Medieval_Environment/Medieval_Castle_Vol1/Maps/CF_01_Demo_Scene.umap``
   * - 2034
     - Modular Medieval Environment
     - ``/Game/Medieval_Env/Maps/Map_NorthenIsle_01.umap``
   * - 2034
     - Modular Medieval Environment
     - ``/Game/Medieval_Env/Maps/Map_MedievalEnv.umap``
   * - 2035
     - Platformer Modular Factory
     - ``/Game/ModularPlatformerIndustrialArea/Map/Factory.umap``
   * - 2036
     - Infinity Weather
     - ``/Game/InfinityWeather/Demo/Maps/DesertMap.umap``
   * - 2036
     - Infinity Weather
     - ``/Game/InfinityWeather/Demo/Maps/RainMap.umap``
   * - 2036
     - Infinity Weather
     - ``/Game/InfinityWeather/Demo/Maps/SnowMap.umap``
   * - 2037
     - Modular Medieval Town with Interior
     - ``/Game/Modular_MedievalTown_WI/Maps/Medieval_Daytime.umap``
   * - 2037
     - Modular Medieval Town with Interior
     - ``/Game/Modular_MedievalTown_WI/Maps/Medieval_Nighttime.umap``
   * - 2038
     - Modular Sci-Fi Village
     - ``/Game/Modular_Sci_Fi/Maps/Prewiev_Sci_fi_Base.umap``
   * - 2039
     - Suburb Neighborhood House Pack
     - ``/Game/SuburbNeighborhoodHousePack/Maps/DemoMap_Day_Lumen.umap``
   * - 2039
     - Suburb Neighborhood House Pack
     - ``/Game/SuburbNeighborhoodHousePack/Maps/DemoMap_Day.umap``
   * - 2039
     - Suburb Neighborhood House Pack
     - ``/Game/SuburbNeighborhoodHousePack/Maps/DemoMap_Night.umap``
   * - 2040
     - Modular Swimming Pool Megapack
     - ``/Game/SwimmingPool/Maps/ChangingRoom_Female.umap``
   * - 2040
     - Modular Swimming Pool Megapack
     - ``/Game/SwimmingPool/Maps/ChangingRoom_Male.umap``
   * - 2040
     - Modular Swimming Pool Megapack
     - ``/Game/SwimmingPool/Maps/Demonstration_AlternatePool.umap``
   * - 2040
     - Modular Swimming Pool Megapack
     - ``/Game/SwimmingPool/Maps/Demonstration_Master.umap``
   * - 2040
     - Modular Swimming Pool Megapack
     - ``/Game/SwimmingPool/Maps/Demonstration_Outdoor.umap``
   * - 2041
     - Forest Gas Station
     - ``/Game/ForestGasStation/Maps/Demo.umap``
   * - 2042
     - School Gym
     - ``/Game/SchoolGym/Maps/SchoolGymDay.umap``
   * - 2043
     - Modular Hotel Corridor
     - ``/Game/HotelCorridor/Maps/Hotel_Corridor.umap``
   * - 2044
     - Grass Hills Landscape
     - ``/Game/GrassHillsLandscape/Maps/Overview/Overview.umap``
   * - 2045
     - Watermills / Nature Environment
     - ``/Game/Watermills/Levels/SampleScene.umap``
   * - 2046
     - Middle East
     - ``/Game/MiddleEast/Maps/MiddleEast.umap``
   * - 2047
     - Chemical Plant & Refinery
     - ``/Game/ChemicalPlantEnv/Maps/Map_ChemicalPlant_1.umap``
   * - 2047
     - Chemical Plant & Refinery
     - ``/Game/ChemicalPlantEnv/Maps/Map_ChemicalPlant_2.umap``
   * - 2048
     - Chinese Landscape
     - ``/Game/Chinese_Landscape/Levels/Chinese_Landscape_Demo.umap``
   * - 2049
     - Slavic Village
     - ``/Game/Village/Maps/Village_SummerNightExample.umap``
   * - 2049
     - Slavic Village
     - ``/Game/Village/Maps/Village.umap``
   * - 2050
     - Opera House Kit
     - ``/Game/OperaHouse/Maps/Demonstration.umap``
   * - 2051
     - Russian Winter Town
     - ``/Game/WinterTown/Maps/RussianWinterTownDemo01.umap``
   * - 2051
     - Russian Winter Town
     - ``/Game/WinterTown/Maps/RussianWinterTownDemo02.umap``
   * - 2052
     - Modular Neighborhood Pack
     - ``/Game/ModularNeighborhood/Maps/Demo_Map.umap``
   * - 2053
     - Asian Temple Pack
     - ``/Game/AsianTemple/Map/LV_Temple_Day.umap``
   * - 2054
     - Urban Abandoned District (Scans)
     - ``/Game/UrbanDistrict/Demo/Maps/Gate/Gate_01_01_P.umap``
   * - 2055
     - Stone Pine Forest
     - ``/Game/StonePineForest/Maps/GooseLand_Map.umap``
   * - 2055
     - Stone Pine Forest
     - ``/Game/StonePineForest/Maps/Mountains_Map.umap``
   * - 2055
     - Stone Pine Forest
     - ``/Game/StonePineForest/Maps/Mountains_Map_LevelDesign.umap``
   * - 2055
     - Stone Pine Forest
     - ``/Game/StonePineForest/Maps/Showcase.umap``
   * - 2055
     - Stone Pine Forest
     - ``/Game/StonePineForest/Maps/Traditional_Map.umap``
   * - 2056
     - Storage House Set
     - ``/Game/StorageHouse/Maps/Demonstration.umap``
   * - 2057
     - Temples of Cambodia
     - ``/Game/TemplesOfCambodia/Demo/Maps/TemplesOfCambodia_01_Exterior/TemplesOfCambodia_01_01_Exterior.umap``
   * - 2057
     - Temples of Cambodia
     - ``/Game/TemplesOfCambodia/Demo/Maps/TemplesOfCambodia_02_Interior/TemplesOfCambodia_02_01_Interior.umap``
   * - 2058
     - Operating Room Pack
     - ``/Game/OperatingRoom/Levels/Operating_Room.umap``
   * - 2059
     - Industrial Area Hangar
     - ``/Game/Hangar/Maps/Hangar.umap``
   * - 2060
     - Modular Asian Medieval City
     - ``/Game/Asian_town/Maps/L_Showcase_map.umap``
   * - 2061
     - The Bazaar
     - ``/Game/Bazaar_Meshingun/Map/LV_Bazaar.umap``
   * - 2062
     - Lookout Tower
     - ``/Game/LookoutTower/Maps/Demo.umap``
   * - 2063
     - Science Fiction Valley Town
     - ``/Game/Sci_FI_Valley_Village/Level/L_showcase_level.umap``
   * - 2064
     - Modular Old Town
     - ``/Game/ModularOldTown/Maps/Old_Town.umap``
   * - 2065
     - Modular Sci-Fi Rocky Swampy Planet
     - ``/Game/ModularSciFi/Levels/LandscapePreview.umap``
   * - 2065
     - Modular Sci-Fi Rocky Swampy Planet
     - ``/Game/ModularSciFi/Levels/PreviewSceneIndoor.umap``
   * - 2066
     - Egyptian Pyramid Modular Kit
     - ``/Game/Pyramids/Levels/L_pyramids.umap``
   * - 2067
     - Dungeon Environment
     - ``/Game/Dungeon/Levels/Dungeon_Demo_00.umap``
   * - 2068
     - Downtown West Modular Pack
     - ``/Game/Downtown_West/Maps/Demo_Environment.umap``
   * - 2069
     - Korean Traditional Palace
     - ``/Game/HwaseongHaenggung/Maps/Demo.umap``
   * - 2070
     - Modular Building Set
     - ``/Game/ModularBuildingSet/Demo_Scene.umap``
   * - 2071
     - SoulCave
     - ``/Game/SoulCave/Maps/LV_Soul_Cave.umap``