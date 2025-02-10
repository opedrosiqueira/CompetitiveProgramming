import cProfile
import pstats
from io import StringIO
import importlib
import sys

# Usage:
# python 01-profiler.py <module_name> <function_name>
# Example:
# get-content .\uva10679.in | python .\01-profiler.py uva10679 main >.\uva10679.out

module_name = sys.argv[1]
function_name = sys.argv[2]

try:
    # Dynamically import the module
    module = importlib.import_module(module_name)

    # Get the specific attribute from the module
    function = getattr(module, function_name)
except ModuleNotFoundError:
    print(f"Module {module_name} not found.")
except AttributeError:
    print(f"Attribute {function_name} not found in module {module_name}.")

# Profile the function
profiler = cProfile.Profile()
profiler.enable()
function()
profiler.disable()

# Capture profiling stats
stats = pstats.Stats(profiler)

# Get the total time from stats
total_time = stats.total_tt
filename = module_name + ".prof"
with open(filename, "a") as f:
    f.write(f"\n{total_time:.6f};{module_name}.{function_name}")
    # stats = pstats.Stats(profiler, stream=f)
    # stats.strip_dirs().sort_stats('cumulative').print_stats()
