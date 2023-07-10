#!/usr/bin/env python
"""
heatwave_metrics.py

Python functions for computing the heatwave metrics from a temperature dataset.

The algorithm is encapsulated in a Python function with additional documentation on its use in other scripts and how the metrics are computed. There is an additional wrapper function "metrics_from_path()" to handle string inputs. This allows the user to develop an xarray solution using the primary function "compute_metrics()"
"""
import xarray
import numpy as np


def indicate_hot_days(temp_ds, threshold):
    """
    Marks days in the temperature input that exceed the daily thresholds.
    [MORE INFO]
    """
    hot_days = np.zeros(temp_ds.values.shape, dtype=int)
    
    # May–September in the Northern Hemisphere and November–March in the Southern Hemisphere
    south_hemisphere = np.ones((int(temp_ds.shape[1]/2), temp_ds.shape[2]))
    south_hemisphere.resize((temp_ds.shape[1], temp_ds.shape[2]))
    north_hemisphere = 1 - south_hemisphere
    
    for index in range(temp_ds.time.values.size):
        day_number = temp_ds.time.values[index].dayofyr
        if 273 >= day_number >= 121:
            # May–September in the Northern Hemisphere
            hot_days[index] = (temp_ds.values[index] > threshold.values[day_number-1])*north_hemisphere
        elif day_number >= 305 or day_number <= 90:
            # November–March in the Southern Hemisphere
            hot_days[index] = (temp_ds.values[index] > threshold.values[day_number-1])*south_hemisphere
    
    return hot_days


def index_heatwaves(timeseries, max_break=1, min_duration=3):
    """
    Identifies the heatwaves in the timeseries
    [MORE INFO]
    """
    timeseries = np.pad(timeseries, 1)
    
    diff_indices = np.where(np.diff(timeseries) != 0)[0] + 1

    in_heatwave = False
    current_hw_index = 1

    hw_indices = np.zeros(timeseries.shape, dtype=np.short)

    for i in range(diff_indices.shape[0]-1):
        index = diff_indices[i]
        next_index = diff_indices[i+1]

        if timeseries[index] == 1 and in_heatwave:
            hw_indices[index:next_index] = current_hw_index
        elif timeseries[index] == 0 and in_heatwave and next_index-index <= max_break:
            hw_indices[index:next_index] = current_hw_index
        elif timeseries[index] == 1 and not in_heatwave and next_index-index >= min_duration:
            in_heatwave = True
            hw_indices[index:next_index] = current_hw_index
        elif in_heatwave:
            current_hw_index += 1
            in_heatwave = False
    return hw_indices[1:-1]


def compute_metrics(temp_ds, control_threshold, temp_path="No path provided.", control_path="No path provided."):
    hot_days = indicate_hot_days(temp_ds, control_threshold)
    indexed_heatwaves = np.zeros(hot_days.shape, dtype=np.short)

    for i in range(hot_days.shape[1]):
        for j in range(hot_days.shape[2]):
            indexed_heatwaves[:, i, j] = index_heatwaves(hot_days[:, i, j])
    
    years = temp_ds.time.values[-1].year - temp_ds.time.values[0].year + 1

    hwf = np.zeros((years, indexed_heatwaves.shape[1], indexed_heatwaves.shape[2]), dtype=int)
    for index in range(years):
        hwf[index] = np.sum(indexed_heatwaves[365*index:365*(index+1)] > 0, axis=0)
    
    meta = {
            "metrics description": f"90th percentile heatwave metrics.",
            "temperature dataset path": temp_path,
            "control dataset path": control_path,
    }
    for key in range(control_threshold.attrs):
        meta[f"threshold-{key}"] = control_threshold.attrs[key]
    
    return xarray.Dataset(
        data_vars=dict(
            HWF=(["year", "lat", "lon"], hwf),
        ),
        coords=dict(
            lon=(["lon"], temp_ds.lon.values),
            lat=(["lat"], temp_ds.lat.values),
            year=np.arange(temp_ds.time.values[0].year, temp_ds.time.values[-1].year+1),
        ),
        attrs=meta,
        )
    
    
def metrics_from_path(temp_ds_path, temp_var_name, control_path, control_var_name) -> xarray.DataArray:
    return compute_metrics(xarray.open_dataset(temp_ds_path)[temp_var_name], xarray.open_dataset(control_path[control_var_name]), temp_path=temp_path, control_path=control_path)