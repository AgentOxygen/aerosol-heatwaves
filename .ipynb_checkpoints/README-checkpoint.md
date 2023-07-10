# Impact of Anthropogenic Aerosols on Patterns of Heatwave Hazard and Exposure

## Overview

This repository has the following directory structure:
```
aerosol-heatwaves
│   README.md
│   environment.yml
|   data_download.md
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
└───notebooks
│   |   README.md
│   │   MainFigures.ipynb
│   └───SupplementFigures.ipynb
|
└───figures
    └───... Figure PNGs ...
```
All packages used in this analysis are included in `environment.yml` which can be used to create a virutal environment for running any and all source code.
All data used is publicly available for download. Access to these datasets and the the directory structure used for running the scripts is detailed in `data_download.md`. Note that all code is dependent on the paths and assertion tests set in `scripts/paths.py`. By default, they follow the structure detailed in `data_download.md`, but can be modified as needed.
The source code for indiviudal figures in the results section of the paper are detailed in `notebooks/MainFigures.ipynb` and supplemental figures are detailed in `notebooks/SupplementFigures.ipynb`.
Original figure images are provided in `figures/` in the PNG format. Note that these figures may have slight aesthetic modifications from those featured in the notebooks, but the results visualized in each are the same.

## Steps for Running this Analysis
