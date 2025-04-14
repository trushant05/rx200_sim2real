from isaacsim import SimulationApp

# Simulation App Config
CONFIG = {
    "width" : 1200,
    "height" : 720,
    "sync_loads" : True,
    "headless" : False,
    "rendere" : "RaytracedLighting"
}

kit = SimulationApp(launch_config=CONFIG)

import carb
import omni

# Validate assets file
from isaacsim.storage.native import is_file
from isaacsim.core.api import World
from isaacsim.core.utils.stage import add_reference_to_stage

# Create world
my_world = World(stage_units_in_meters=1.0)
my_world.scene.add_default_ground_plane()

# Absolute path to the asset
usd_path = "/home/workspaces/sim2real/assets/robots/franka/franka_flatten.usd"

try: 
    result = is_file(usd_path)
except: 
    result = False

if result:
    add_reference_to_stage(usd_path=usd_path, prim_path="/World/Franka")
else:
    carb.log_error(
        f"the usd path {usd_path} could not be opened, please make sure that {usd_path} is a valid usd file."
    )
    kit.close()
    sys.exit()

# Wait two frames so that stage starts loading
kit.update()
kit.update()

print("Loading stage...")
from isaacsim.core.utils.stage import is_stage_loading

while is_stage_loading():
    kit.update()
print("Loading Complete")

while kit.is_running():
    kit.update()

kit.close()
