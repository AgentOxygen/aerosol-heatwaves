#!/usr/bin/env python
"""
'directory_structure.py'

Author: Cameron Cummins
Email: cameron.cummins@utexas.edu

Manages the directory structure of the data repository for the Aerosol-Heatwave project.

'DATA_DIR' should be modified with a *global* path that points to where the repository should be generated.

Note that global here means a path that can be accessed anywhere in the filesystem (usually starts with
a forward slash '/'). Local paths (such as starting with '../') will likely cause errors.

All variables created in this script with the suffix '_DIR' are treated as strings
that point to a valid directory. An error is raised if no valid directory is found 
at that path.

This script may be imported to obtain the checked paths (imported automatically my 'paths.py').
This script may be run in a Python shell to automatically generate any missing directories.
"""
from os import makedirs
from os.path import isdir


# ======== HEAD DIRECTORY FOR THE ENTIRE REPOSITORY ========
DATA_DIR = "/projects/dgs/persad_research/AER_HEATWAVE_DATA/"
# This should be modified with a global path that points to where you want to generate
# the data repository. I have left mine, which is specific to my filesystem, for clarity.

# ======================= Directories =======================
LENS1_DIR = DATA_DIR + "LENS1/"

ALL_DIR = LENS1_DIR + "ALL/"
XAER_DIR = LENS1_DIR + "XAER/"
PI_DIR = LENS1_DIR + "PREINDUSTRIAL/"
LANDFRAC_DIR = LENS1_DIR + "LANDFRAC/"

ALL_TREFHTMN_DIR = ALL_DIR + "TREFHTMN/"
ALL_TREFHTMX_DIR = ALL_DIR + "TREFHTMX/"
XAER_TREFHTMN_DIR = XAER_DIR + "TREFHTMN/"
XAER_TREFHTMX_DIR = XAER_DIR + "TREFHTMX/"
PI_TREFHTMN_DIR = PI_DIR + "TREFHTMN/"
PI_TREFHTMX_DIR = PI_DIR + "TREFHTMX/"

MERRA2_DIR = DATA_DIR + "MERRA2/"
MERRA2_UP_DIR = DATA_DIR + "MERRA2_UPSCALED/"

MERRA2_TREFHTMN_DIR = MERRA2_DIR + "TREFHTMN/"
MERRA2_TREFHTMX_DIR = MERRA2_DIR + "TREFHTMX/"
MERRA2_UP_TREFHTMN_DIR = MERRA2_UP_DIR + "TREFHTMN/"
MERRA2_UP_TREFHTMX_DIR = MERRA2_UP_DIR + "TREFHTMX/"

POP_DENSITY_DIR = DATA_DIR + "POP_DENSITY/"

HW_DIR = DATA_DIR + "HEATWAVE_OUTPUT/"

THRESHOLDS_DIR = HW_DIR + "THRESHOLDS/"
METRICS_DIR = HW_DIR + "METRICS/"

ALL_METRICS_DIR = METRICS_DIR + "ALL/"
XAER_METRICS_DIR = METRICS_DIR + "XAER/"
PI_METRICS_DIR = METRICS_DIR + "PREINDUSTRIAL/"
MERRA2_UP_METRICS_DIR = METRICS_DIR + "MERRA2_UPSCALED/"

# Copies all of the variables created in this Python namespace
variables = locals().copy()
# Filters out the directory variables created above with the '_DIR' suffix
DATA_DIRECTORIES = [(name, variables[name]) for name in variables.keys() if "_DIR" in name]

del variables

# Called when the script is executed in a Python shell
if __name__ == '__main__':
    for var_name, path in DATA_DIRECTORIES:
        if not isdir(path):
            print(f"No directory for '{var_name}', creating directory at '{path}'")
            makedirs(path)

# Make sure that the directory paths are valid.
for var_name, path in DATA_DIRECTORIES:
    if not isdir(path):
        raise FileNotFoundError(f"Directory not found for variable '{var_name}' at path '{path}'. Either fix the directory manually or run 'directory_structure.py' to automatically generate all missing directories.")

print(f"(directory_structure.py) Directory structure for data repository generated at 'DATA_DIR' = '{DATA_DIR}'")
print(f"(directory_structure.py) All {len(DATA_DIRECTORIES)} sub-directory paths are valid.")

