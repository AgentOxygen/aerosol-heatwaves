#!/usr/bin/env python
"""
heatwave_thresholds.py

Python functions for computing the daily temperature threshold that defines an extreme heat day and may constitute a portion of a heatwave.

The algorithm is encapsulated in a Python function with additional documentation on its use in other scripts and how the threshold is computed. There is an additional wrapper function "threshold_from_path()" to handle string inputs. This allows the user to develop an xarray solution using the primary function "compute_threshold()"
"""
import xarray
import numpy as np


def compute_threshold(temperature_data: xarray.DataArray, percentile:float=0.9, percentile_range:int=7, temp_path="No path provided.", control_path="No path provided.") -> xarray.DataArray:
    """
    ADD MORE INFO
    
    percentile_range -> days before and after the day of intereset when computing the percentile to include into the pool
    """
    init_year = temperature_data.time.values[0].year
    year_range = temperature_data.time.values[-1].year - init_year + 1
    day_of_year = np.zeros((365, year_range), int) - 1

    for index in range(temperature_data.time.values.size):
        date = temperature_data.time.values[index]
        day_of_year[date.dayofyr-1, date.year - init_year] = index

    annual_threshold = np.zeros((365, temperature_data.lat.size, temperature_data.lon.size))
    expanded_indices = np.zeros(365+2*percentile_range, int)

    for index in range(percentile_range):
        expanded_indices[index] = 364 - index
        expanded_indices[index+365+percentile_range] = index

    for index in range(365):
        expanded_indices[index+percentile_range] = index

    for index in range(day_of_year.shape[0]):
        times = np.concatenate([day_of_year[expanded_indices[i]] for i in range(index, index+2*percentile_range)])
        quantiles = np.quantile(np.array([temperature_data.values[i] for i in times if i >= 0]), percentile, axis=0)
        annual_threshold[index] = quantiles

    return xarray.Dataset(
        data_vars=dict(
            threshold=(["day", "lat", "lon"], annual_threshold),
        ),
        coords=dict(
            lon=(["lon"], temperature_data.lon.values),
            lat=(["lat"], temperature_data.lat.values),
            day=np.arange(0, 365),
        ),
        attrs={
            "description":f"{int(percentile*100)}th percentile temperatures using {percentile_range}-day rolling average.",
            "temperature dataset path": temp_path,
            "control dataset path": control_path
        },
    )


def threshold_from_path(temperature_path: str, threshold_path: str, percentile: float, percentile_range: int) -> xarray.DataArray:
    return compute_threshold(xarray.open_dataset(temperature_path), percentile, percentile_range, temp_path=temperature_path, control_path=threshold_path)
