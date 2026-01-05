# Data Files Overview

| File | Purpose | Usage | Notes |
| --- | --- | --- | --- |
| bounding_boxes.json | Bounding boxes and dimensions for building/element types used during city generation. | CityGenerator via `_load_bounding_boxes()` (simworld/citygen/city/city_generator.py); configured as `citygen.input_bounding_boxes` in simworld/config/default.yaml. | Required when generating layouts or loading progen worlds. |
| description_map.json | Textual descriptions for assets to support retrieval/placement from natural language. | AssetsRP (simworld/assets_rp/AssetsRP.py) through ReferenceAssetsRetriever. | Used to match prompts to assets and surroundings. |
| predefined_roads.json | Pre-baked road layout for city generation. | Point `citygen.input_roads` or map loaders to this file to use it. | Optional fixed layout input. |
| vehicle_types.json | Vehicle archetypes (length/width/reference blueprint) for traffic simulation. | VehicleManager (simworld/traffic/manager/vehicle_manager.py) via `traffic.vehicle.model_file_path`. | Populate traffic spawns with varied vehicle types. |
| building_images/ | Image set for asset retrieval (CLIP matching) in AssetsRP. | AssetsRP uses `assets_rp.input_sample_dataset` (default `building_images`) when calling `retrieve_target_asset`. | Add or replace images here to steer retrieval results. |

