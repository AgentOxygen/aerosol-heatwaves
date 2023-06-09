# Python Scripts for Executing and Verifying Analysis

## Overview

```
aerosol-heatwaves
│   ...
│   
└───scripts
│   |   README.md
│   │   compute_thresholds.py
│   │   compute_metrics.py
|   |   compute_weighted.py
|   |   regrid_population.py
│   │   paths.py
│   │
│   └───heatwave_scripts
│         |   README.md
│         │   heatwave_threshold.py
│         └───heatwave_metrics.py
│   
|    ...
```

This directory contains all necessary scripts for running the analysis. Each script executes assertion statements in `paths.py` before attempting to run. They should be run in the following order to avoid error:

1. `regrid_population.py` regrids the population data to fit the heatwave data. This is necessary for `compute_weighted.py` to run without error.
2. `compute_thresholds.py` utilizes the functions contained in `heatwave_scripts/heatwave_threshold.py` to compute the heatwave thresholds for the data of interest. The script runs in parallel and can be tuned to run more efficiently over multiple cores.
3. `compute_metrics.py` utilizes the functions contained in `heatwave_scripts/heatwave_metrics.py` to compute the heatwave hazard metrics for the data of interest using the thresholds produced by `compute_thresholds.py`. The script runs in parallel and can be tuned to run more efficiently over multiple cores.
4. `compute_weighted.py` copies the output of `compute_metrics.py` and weights each grid cell's value by the population count to obtain heatwave exposure metrics.

`paths.py` contains paths to the netCDF files, both original input and script output, and other data. Running or importing this script checks the validity of the paths to downloaded data, but not output data (this is be checked by separate functions).