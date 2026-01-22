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

For example, run the following command from the extracted UE server directory:

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

The following table lists the scenes and their corresponding Map Paths included in the additional environments version of SimWorld:

.. list-table::
   :header-rows: 1
   :widths: 5 10 40 45

   * - ID
     - ChunkID
     - Asset Library
     - Map Path
   * - 1
     - 2001
     - QA Modular Parking
     - ``/Game/QA_ModularParking/Maps/Map_demonstration.umap``
   * - 2
     - 2002
     - University Classroom Interior Environment / School Room
     - ``/Game/UNIVERSITY_CLASSROOM/Levels/Showcase.umap``
   * - 3
     - 2003
     - Chinese Water Town Ver.1
     - ``/Game/ChineseWaterTown/Ver1/Map/DemoMap.umap``
   * - 4
     - 2004
     - Venice – Fast Building
     - ``/Game/Venice_fast_building/Maps/Showcase.umap``
   * - 5
     - 2005
     - Low Poly Medieval Interior and Constructions
     - ``/Game/LowPolyMedievalConstructions/Maps/Map_1.umap``
   * - 6
     - 2005
     - Low Poly Medieval Interior and Constructions
     - ``/Game/LowPolyMedievalConstructions/Maps/Map_2.umap``
   * - 7
     - 2005
     - Low Poly Medieval Interior and Constructions
     - ``/Game/LowPolyMedievalConstructions/Maps/Map_3.umap``
   * - 8
     - 2005
     - Low Poly Medieval Interior and Constructions
     - ``/Game/LowPolyMedievalConstructions/Maps/Map_8.umap``
   * - 9
     - 2005
     - Low Poly Medieval Interior and Constructions
     - ``/Game/LowPolyMedievalConstructions/Maps/Map_9.umap``
   * - 10
     - 2005
     - Low Poly Medieval Interior and Constructions
     - ``/Game/LowPolyMedievalConstructions/Maps/Map_4_Top-Down.umap``
   * - 11
     - 2005
     - Low Poly Medieval Interior and Constructions
     - ``/Game/LowPolyMedievalConstructions/Maps/Map_5_Top-Down.umap``
   * - 12
     - 2005
     - Low Poly Medieval Interior and Constructions
     - ``/Game/LowPolyMedievalConstructions/Maps/Map_6_Top-Down.umap``
   * - 13
     - 2005
     - Low Poly Medieval Interior and Constructions
     - ``/Game/LowPolyMedievalConstructions/Maps/Map_7_Top-Down.umap``
   * - 14
     - 2006
     - Atmospheric Modular Underground Car Park & Hallways
     - ``/Game/ParkingGarage/Maps/UndergroundParking.umap``
   * - 15
     - 2007
     - Tokyo Stylized Environment
     - ``/Game/TokyoStylizedEnvironment/Maps/Tokyo.umap``
   * - 16
     - 2008
     - Lighthouse Island – High Quality Environment
     - ``/Game/Lighthouse_Island/Levels/Lighthouse_Demo_00.umap``
   * - 17
     - 2009
     - Rocket Launch Command Center
     - ``/Game/Nimikko_CommandCenter/Scenes/CommandCenter.umap``
   * - 18
     - 2010
     - Desert Ruins
     - ``/Game/desert_ruins/maps/Showcase.umap``
   * - 19
     - 2011
     - Wild West City
     - ``/Game/Wild_West/Maps/WildWest.umap``
   * - 20
     - 2012
     - Euro Champions Football Stadium
     - ``/Game/ErikStadium/Maps/Stadium.umap``
   * - 21
     - 2013
     - Next Gen Modular Victorian Neoclassical City
     - ``/Game/ModularVictorianCity/Maps/Demo_Map.umap``
   * - 22
     - 2014
     - Modular Gothic / Fantasy Environment
     - ``/Game/ModularGothicFantasyEnvironment/Maps/DemoMapDay.umap``
   * - 23
     - 2014
     - Modular Gothic / Fantasy Environment
     - ``/Game/ModularGothicFantasyEnvironment/Maps/DemoMapNight.umap``
   * - 24
     - 2015
     - Bunker
     - ``/Game/Bunker/Maps/demonstration_BUNKER.umap``
   * - 25
     - 2016
     - Fantasy Medieval Castle Kit
     - ``/Game/CastleRiver/Maps/Demonstration.umap``
   * - 26
     - 2017
     - Roof – City Pack
     - ``/Game/RoofProps/Scenes/Demo_Roof.umap``
   * - 27
     - 2018
     - Fantasy Cave Environment Set
     - ``/Game/Cave/Maps/Demonstration.umap``
   * - 28
     - 2019
     - Modular Temple Plaza 4K PBR
     - ``/Game/ModularTemplePlaza/Maps/ConceptMap.umap``
   * - 29
     - 2020
     - Ancient Ruins
     - ``/Game/AnchientRuins/Maps/AncientRuins.umap``
   * - 30
     - 2021
     - Racing Track Winter Landscape
     - ``/Game/racing_track/map/racing_track.umap``
   * - 31
     - 2022
     - Ultimate Farming
     - ``/Game/UltimateFarming/Maps/TinyFields.umap``
   * - 32
     - 2023
     - Hospital Inside
     - ``/Game/hospital/map/demo.umap``
   * - 33
     - 2024
     - Modular Industrial Area
     - ``/Game/IndustrialArea/Maps/IndustrialArea.umap``
   * - 34
     - 2025
     - Greek Island
     - ``/Game/Greek_island/Level/L_greek_island.umap``
   * - 35
     - 2026
     - Supermarket
     - ``/Game/MMSupermarket/Maps/Supermarket_Map.umap``
   * - 36
     - 2027
     - QA Holding Cells
     - ``/Game/QA_HoldingCells/Maps/QA_Holding_Cells_A.umap``
   * - 37
     - 2027
     - QA Holding Cells
     - ``/Game/QA_HoldingCells/Maps/QA_Holding_Cells_B.umap``
   * - 38
     - 2028
     - Victorian Train Station & Railroad
     - ``/Game/TrainStation/Maps/Demonstration.umap``
   * - 39
     - 2028
     - Modular Urban City Asset Megapack
     - ``/Game/TrainStation/Maps/TrainStation_Optimised.umap``
   * - 40
     - 2029
     - Old Factory
     - ``/Game/Old_Factory_01/Maps/Demoscene_01.umap``
   * - 41
     - 2030
     - Container Yard Environment Set
     - ``/Game/ContainerYard/Maps/Demonstration.umap``
   * - 42
     - 2030
     - Container Yard Environment Set
     - ``/Game/ContainerYard/Maps/Demonstration_Day.umap``
   * - 43
     - 2031
     - Modular Courtyard 1.0
     - ``/Game/ModularCourtyard/Maps/SampleScene_overcast.umap``
   * - 44
     - 2031
     - Modular Courtyard 1.0
     - ``/Game/ModularCourtyard/Maps/SampleScene_sanny.umap``
   * - 45
     - 2032
     - Brushify – Arctic Pack
     - ``/Game/Brushify/Maps/Arctic/Arctic.umap``
   * - 46
     - 2033
     - Modular Medieval Environment
     - ``/Game/Medieval_Environment/Real_Landscape/Default/Maps/Default_Demo.umap``
   * - 47
     - 2033
     - Modular Medieval Environment
     - ``/Game/Medieval_Environment/Medieval_Castle_Vol1/Maps/CF_01_Demo_Scene.umap``
   * - 48
     - 2034
     - Modular Medieval Environment
     - ``/Game/Medieval_Env/Maps/Map_NorthenIsle_01.umap``
   * - 49
     - 2034
     - Modular Medieval Environment
     - ``/Game/Medieval_Env/Maps/Map_MedievalEnv.umap``
   * - 50
     - 2035
     - Platformer Modular Factory
     - ``/Game/ModularPlatformerIndustrialArea/Map/Factory.umap``
   * - 51
     - 2036
     - Infinity Weather
     - ``/Game/InfinityWeather/Demo/Maps/DesertMap.umap``
   * - 52
     - 2036
     - Infinity Weather
     - ``/Game/InfinityWeather/Demo/Maps/RainMap.umap``
   * - 53
     - 2036
     - Infinity Weather
     - ``/Game/InfinityWeather/Demo/Maps/SnowMap.umap``
   * - 54
     - 2037
     - Modular Medieval Town with Interior
     - ``/Game/Modular_MedievalTown_WI/Maps/Medieval_Daytime.umap``
   * - 55
     - 2037
     - Modular Medieval Town with Interior
     - ``/Game/Modular_MedievalTown_WI/Maps/Medieval_Nighttime.umap``
   * - 56
     - 2038
     - Modular Sci-Fi Village
     - ``/Game/Modular_Sci_Fi/Maps/Prewiev_Sci_fi_Base.umap``
   * - 57
     - 2039
     - Suburb Neighborhood House Pack
     - ``/Game/SuburbNeighborhoodHousePack/Maps/DemoMap_Day_Lumen.umap``
   * - 58
     - 2039
     - Suburb Neighborhood House Pack
     - ``/Game/SuburbNeighborhoodHousePack/Maps/DemoMap_Day.umap``
   * - 59
     - 2039
     - Suburb Neighborhood House Pack
     - ``/Game/SuburbNeighborhoodHousePack/Maps/DemoMap_Night.umap``
   * - 60
     - 2040
     - Modular Swimming Pool Megapack
     - ``/Game/SwimmingPool/Maps/ChangingRoom_Female.umap``
   * - 61
     - 2040
     - Modular Swimming Pool Megapack
     - ``/Game/SwimmingPool/Maps/ChangingRoom_Male.umap``
   * - 62
     - 2040
     - Modular Swimming Pool Megapack
     - ``/Game/SwimmingPool/Maps/Demonstration_AlternatePool.umap``
   * - 63
     - 2040
     - Modular Swimming Pool Megapack
     - ``/Game/SwimmingPool/Maps/Demonstration_Master.umap``
   * - 64
     - 2040
     - Modular Swimming Pool Megapack
     - ``/Game/SwimmingPool/Maps/Demonstration_Outdoor.umap``
   * - 65
     - 2041
     - Forest Gas Station
     - ``/Game/ForestGasStation/Maps/Demo.umap``
   * - 66
     - 2042
     - School Gym
     - ``/Game/SchoolGym/Maps/SchoolGymDay.umap``
   * - 67
     - 2043
     - Modular Hotel Corridor
     - ``/Game/HotelCorridor/Maps/Hotel_Corridor.umap``
   * - 68
     - 2044
     - Grass Hills Landscape
     - ``/Game/GrassHillsLandscape/Maps/Overview/Overview.umap``
   * - 69
     - 2045
     - Watermills / Nature Environment
     - ``/Game/Watermills/Levels/SampleScene.umap``
   * - 70
     - 2046
     - Middle East
     - ``/Game/MiddleEast/Maps/MiddleEast.umap``
   * - 71
     - 2047
     - Chemical Plant & Refinery
     - ``/Game/ChemicalPlantEnv/Maps/Map_ChemicalPlant_1.umap``
   * - 72
     - 2047
     - Chemical Plant & Refinery
     - ``/Game/ChemicalPlantEnv/Maps/Map_ChemicalPlant_2.umap``
   * - 73
     - 2048
     - Chinese Landscape
     - ``/Game/Chinese_Landscape/Levels/Chinese_Landscape_Demo.umap``
   * - 74
     - 2049
     - Slavic Village
     - ``/Game/Village/Maps/Village_SummerNightExample.umap``
   * - 75
     - 2049
     - Slavic Village
     - ``/Game/Village/Maps/Village.umap``
   * - 76
     - 2050
     - Opera House Kit
     - ``/Game/OperaHouse/Maps/Demonstration.umap``
   * - 77
     - 2051
     - Russian Winter Town
     - ``/Game/WinterTown/Maps/RussianWinterTownDemo01.umap``
   * - 78
     - 2051
     - Russian Winter Town
     - ``/Game/WinterTown/Maps/RussianWinterTownDemo02.umap``
   * - 79
     - 2052
     - Modular Neighborhood Pack
     - ``/Game/ModularNeighborhood/Maps/Demo_Map.umap``
   * - 80
     - 2053
     - Asian Temple Pack
     - ``/Game/AsianTemple/Map/LV_Temple_Day.umap``
   * - 81
     - 2054
     - Urban Abandoned District (Scans)
     - ``/Game/UrbanDistrict/Demo/Maps/Gate/Gate_01_01_P.umap``
   * - 82
     - 2055
     - Stone Pine Forest
     - ``/Game/StonePineForest/Maps/GooseLand_Map.umap``
   * - 83
     - 2055
     - Stone Pine Forest
     - ``/Game/StonePineForest/Maps/Mountains_Map.umap``
   * - 84
     - 2055
     - Stone Pine Forest
     - ``/Game/StonePineForest/Maps/Mountains_Map_LevelDesign.umap``
   * - 85
     - 2055
     - Stone Pine Forest
     - ``/Game/StonePineForest/Maps/Showcase.umap``
   * - 86
     - 2055
     - Stone Pine Forest
     - ``/Game/StonePineForest/Maps/Traditional_Map.umap``
   * - 87
     - 2056
     - Storage House Set
     - ``/Game/StorageHouse/Maps/Demonstration.umap``
   * - 88
     - 2057
     - Temples of Cambodia
     - ``/Game/TemplesOfCambodia/Demo/Maps/TemplesOfCambodia_01_Exterior/TemplesOfCambodia_01_01_Exterior.umap``
   * - 89
     - 2057
     - Temples of Cambodia
     - ``/Game/TemplesOfCambodia/Demo/Maps/TemplesOfCambodia_02_Interior/TemplesOfCambodia_02_01_Interior.umap``
   * - 90
     - 2058
     - Operating Room Pack
     - ``/Game/OperatingRoom/Levels/Operating_Room.umap``
   * - 91
     - 2059
     - Industrial Area Hangar
     - ``/Game/Hangar/Maps/Hangar.umap``
   * - 92
     - 2060
     - Modular Asian Medieval City
     - ``/Game/Asian_town/Maps/L_Showcase_map.umap``
   * - 93
     - 2061
     - The Bazaar
     - ``/Game/Bazaar_Meshingun/Map/LV_Bazaar.umap``
   * - 94
     - 2062
     - Lookout Tower
     - ``/Game/LookoutTower/Maps/Demo.umap``
   * - 95
     - 2063
     - Science Fiction Valley Town
     - ``/Game/Sci_FI_Valley_Village/Level/L_showcase_level.umap``
   * - 96
     - 2064
     - Modular Old Town
     - ``/Game/ModularOldTown/Maps/Old_Town.umap``
   * - 97
     - 2065
     - Modular Sci-Fi Rocky Swampy Planet
     - ``/Game/ModularSciFi/Levels/LandscapePreview.umap``
   * - 98
     - 2065
     - Modular Sci-Fi Rocky Swampy Planet
     - ``/Game/ModularSciFi/Levels/PreviewSceneIndoor.umap``
   * - 99
     - 2066
     - Egyptian Pyramid Modular Kit
     - ``/Game/Pyramids/Levels/L_pyramids.umap``
   * - 100
     - 2067
     - Dungeon Environment
     - ``/Game/Dungeon/Levels/Dungeon_Demo_00.umap``
   * - 101
     - 2068
     - Downtown West Modular Pack
     - ``/Game/Downtown_West/Maps/Demo_Environment.umap``
   * - 102
     - 2069
     - Korean Traditional Palace
     - ``/Game/HwaseongHaenggung/Maps/Demo.umap``
   * - 103
     - 2070
     - Modular Building Set
     - ``/Game/ModularBuildingSet/Demo_Scene.umap``
   * - 104
     - 2071
     - SoulCave
     - ``/Game/SoulCave/Maps/LV_Soul_Cave.umap``