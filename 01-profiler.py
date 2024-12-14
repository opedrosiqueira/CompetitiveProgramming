import cProfile
import pstats
from io import StringIO
import importlib
import sys

module_name = sys.argv[1]
attribute_name = sys.argv[2]

try:
    # Dynamically import the module
    module = importlib.import_module(module_name)

    # Get the specific attribute from the module
    function = getattr(module, attribute_name)

    print(f"Successfully imported {attribute_name} from {module_name}")
    print(f"Attribute: {function}")
except ModuleNotFoundError:
    print(f"Module {module_name} not found.")
except AttributeError:
    print(f"Attribute {attribute_name} not found in module {module_name}.")

# Profile the function
profiler = cProfile.Profile()
profiler.enable()
function()
profiler.disable()

# Capture profiling stats
stats = pstats.Stats(profiler)

# Get the total time from stats
total_time = stats.total_tt
print(f"\n{total_time:.6f};{module_name}.{attribute_name}")
