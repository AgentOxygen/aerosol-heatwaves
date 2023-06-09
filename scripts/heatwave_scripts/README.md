# Heatwave Metric/Threshold Source Code
## Overview

```
aerosol-heatwaves
│   ...
│   
└───scripts
│   |   ...
│   │
│   └───heatwave_scripts
│         |   README.md
│         │   heatwave_threshold.py
│         └───heatwave_metrics.py
│   
|    ...
```

These scripts are derived from source code provided by Dr. Jane Baldwin and her research on compounding heatwave events: 

Baldwin, J. W., Dessy, J. B., Vecchi, G. A., & Oppenheimer, M. (2019). Temporally compound heat wave events and global warming: An emerging hazard. Earth's Future, 7, 411– 427. https://doi.org/10.1029/2018EF000989

- `heatwave_threshold.py` computes the temperature threshold for a heatwave event accounting for variations in seasonality and applies separate computations to the Northern and Southern hemisphere.
- `heatwave_metrics.py` utilizes the output from `heatwave_threshold.py` to compute heatwave frequency and duration for a given temperature input.