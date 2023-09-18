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
import sys
sys.path.append('./heatwave_scripts/')
from heatwave_metrics import compute_metrics
from heatwave_threshold import threshold_from_path


if __name__ == '__main__':
    
#     if not isfile(paths.CONTROL_TREFHTMN_THRESHOLD_NETCDF):
#         print(f"Computing {paths.CONTROL_TREFHTMN_THRESHOLD_NETCDF}")
#         ds = threshold_from_path(paths.CONTROL_TREFHTMN_NETCDF, "TREFHTMN", 0.9)
#         ds.to_netcdf(paths.CONTROL_TREFHTMN_THRESHOLD_NETCDF)
    
    # if not isfile(paths.CONTROL_TREFHTMX_THRESHOLD_NETCDF):
    #     print(f"Computing {paths.CONTROL_TREFHTMX_THRESHOLD_NETCDF}")
    #     ds = threshold_from_path(paths.CONTROL_TREFHTMX_NETCDF, "TREFHTMX", 0.9)
    #     ds.to_netcdf(paths.CONTROL_TREFHTMX_THRESHOLD_NETCDF)
    
    control_trefhtmn_threshold = xarray.open_dataset(paths.CONTROL_TREFHTMN_THRESHOLD_NETCDF)["threshold"].load()
    
#     for file in listdir(paths.ALL_TREFHTMN_DATA):
#         temp_path = paths.ALL_TREFHTMN_DATA + file
#         out_path = paths.ALL_TREFHTMN_HEAT_METRICS + f"{file}_hw.nc"
        
#         if not isfile(out_path):
#             print(f"Computing {out_path}")
#             ds = compute_metrics(xarray.open_dataset(temp_path)["TREFHTMN"], control_trefhtmn_threshold, temp_path, paths.CONTROL_TREFHTMN_THRESHOLD_NETCDF)
#             ds.to_netcdf(out_path)
    
    for file in listdir(paths.XAER_TREFHTMN_DATA):
        temp_path = paths.XAER_TREFHTMN_DATA + file
        out_path = paths.XAER_TREFHTMN_HEAT_METRICS + f"{file}_hw.nc"
        
        if not isfile(out_path):
            print(f"Computing {out_path}")
            ds = compute_metrics(xarray.open_dataset(temp_path)["TREFHTMN"], control_trefhtmn_threshold, temp_path, paths.CONTROL_TREFHTMX_THRESHOLD_NETCDF)
            ds.to_netcdf(out_path)
            
    control_trefhtmx_threshold = xarray.open_dataset(paths.CONTROL_TREFHTMX_THRESHOLD_NETCDF)["threshold"].load()
    
    for file in listdir(paths.ALL_TREFHTMX_DATA):
        temp_path = paths.ALL_TREFHTMX_DATA + file
        out_path = paths.ALL_TREFHTMX_HEAT_METRICS + f"{file}_hw.nc"
        
        if not isfile(out_path):
            print(f"Computing {out_path}")
            ds = compute_metrics(xarray.open_dataset(temp_path)["TREFHTMX"], control_trefhtmx_threshold, temp_path, paths.CONTROL_TREFHTMX_THRESHOLD_NETCDF)
            ds.to_netcdf(out_path)
        
    for file in listdir(paths.XAER_TREFHTMX_DATA):
        temp_path = paths.XAER_TREFHTMX_DATA + file
        out_path = paths.XAER_TREFHTMN_HEAT_METRICS + f"{file}_hw.nc"
        
        if not isfile(out_path):
            print(f"Computing {out_path}")
            ds = compute_metrics(xarray.open_dataset(temp_path)["TREFHTMX"], control_trefhtmx_threshold, temp_path, paths.CONTROL_TREFHTMX_THRESHOLD_NETCDF)
            ds.to_netcdf(out_path)
    
    print("Done.")
    
    
