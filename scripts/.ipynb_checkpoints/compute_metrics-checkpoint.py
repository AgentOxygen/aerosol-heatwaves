#!/usr/bin/env python
"""
compute_metrics.py

Python script for computing the relevant heatwave metrics for this particular study of LENS data.
"""
import paths
import xarray
import numpy as np
from os import listdir
from os.path import isfile
sys.path.append('/heatwave_scripts/')
from heatwave_metrics import metrics_from_path
from heatwave_threshold import threshold_from_path


if __name__ == '__main__':
    
    if not isfile(paths.CONTROL_TREFHTMN_THRESHOLD_NETCDF):
        print(f"Generating {paths.CONTROL_TREFHTMN_THRESHOLD_NETCDF}")
        threshold_from_path(paths.CONTROL_TREFHTMN_NETCDF, paths.CONTROL_TREFHTMN_THRESHOLD_NETCDF, 0.9, 7).to_netcdf(paths.CONTROL_TREFHTMN_THRESHOLD_NETCDF)
    
    if not isfile(paths.CONTROL_TREFHTMX_THRESHOLD_NETCDF):
        print(f"Generating {paths.CONTROL_TREFHTMX_THRESHOLD_NETCDF}")
        threshold_from_path(paths.CONTROL_TREFHTMX_NETCDF, paths.CONTROL_TREFHTMX_THRESHOLD_NETCDF, 0.9, 7).to_netcdf(paths.CONTROL_TREFHTMX_THRESHOLD_NETCDF)
    
    for file in listdir(paths.ALL_TREFHTMN_DATA):
        temp_path = paths.ALL_TREFHTMN_DATA + file
        out_path = paths.ALL_TREFHTMN_HEAT_METRICS + f"{file}_hw.nc"
        
        if not isfile(out_path):
            print(f"Generating {out_path}")
            metrics_from_path(temp_path, "TREFHTMN", path.CONTROL_TREFHTMN_THRESHOLD_NETCDF, "threshold").to_netcdf(out_path)
    
    for file in listdir(paths.ALL_TREFHTMX_DATA):
        temp_path = paths.ALL_TREFHTMX_DATA + file
        out_path = paths.ALL_TREFHTMN_HEAT_METRICS + f"{file}_hw.nc"
        
        if not isfile(out_path):
            print(f"Generating {out_path}")
            metrics_from_path(temp_path, "TREFHTMX", path.CONTROL_TREFHTMX_THRESHOLD_NETCDF, "threshold").to_netcdf(out_path)
    
    print("Done.")
    
    