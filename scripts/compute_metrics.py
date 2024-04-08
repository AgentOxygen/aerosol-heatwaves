#!/usr/bin/env python
"""
compute_metrics.py

Python script for computing the relevant heatwave metrics for this particular study of LENS1 data.
"""
import xarray
from distributed import Client
import sys
sys.path.insert(1, '../heatwave_analysis_package/src')
import hdp
import cftime
import numpy as np


if __name__ == '__main__':
    client = Client('localhost:8786')

    INPUT_DIR = "/projects/dgs/persad_research/SIMULATION_DATA/ZARR/LENS1/SIM_VARIABLES/"
    OUTPUT_DIR = "/projects/dgs/persad_research/SIMULATION_DATA/ZARR/LENS1/HEAT_OUTPUTS/"

    pi_time_start = cftime.DatetimeNoLeap(1920, 1, 1, 0, 0, 0, 0, has_year_zero=True)
    pi_time_end = cftime.DatetimeNoLeap(2200, 12, 31, 0, 0, 0, 0, has_year_zero=True)
    tmin_pi_path = f"{INPUT_DIR}preindustrial_day_TREFHTMN.zarr"

    tmin_pi_ds = xarray.open_zarr(tmin_pi_path)["TREFHTMN"]
    tmin_pi_ds = tmin_pi_ds.sel(time=slice(pi_time_start, pi_time_end))

    print("Computing threshold...", end=" ")
    tmin_threshold = hdp.compute_threshold(tmin_pi_ds, np.arange(0.9, 1, 0.01), temp_path=tmin_pi_path)
    tmin_threshold.chunk(dict(percentile=-1, day=-1, lat=-1, lon=-1)).to_zarr(f"{OUTPUT_DIR}CESM1_LE_TREFHTMN_THRESHOLD.zarr", consolidated=True)
    print("Done.")

    tmin_all_path = f"{INPUT_DIR}all_day_TREFHTMN.zarr"
    tmin_xaer_path = f"{INPUT_DIR}xaer_day_TREFHTMN.zarr"
    tmin_xghg_path = f"{INPUT_DIR}xghg_day_TREFHTMN.zarr"

    tmin_all_ds = xarray.open_zarr(tmin_all_path)["TREFHTMN"]
    tmin_xaer_ds = xarray.open_zarr(tmin_xaer_path)["TREFHTMN"]
    tmin_xghg_ds = xarray.open_zarr(tmin_xghg_path)["TREFHTMN"]

    all_hw_ds = []
    xaer_hw_ds = []
    xghg_hw_ds = []

    print("Computing metrics for members:", end=" ")
    for member in tmin_xghg_ds.member:
        all_hw_ds.append(hdp.compute_heatwave_metrics(tmin_all_ds.sel(member=member).compute(), tmin_threshold.sel(percentile=[0.9, 0.95], method="nearest")))
        xaer_hw_ds.append(hdp.compute_heatwave_metrics(tmin_xaer_ds.sel(member=member).compute(), tmin_threshold.sel(percentile=[0.9, 0.95], method="nearest")))
        xghg_hw_ds.append(hdp.compute_heatwave_metrics(tmin_xghg_ds.sel(member=member).compute(), tmin_threshold.sel(percentile=[0.9, 0.95], method="nearest")))
        print(member, end=", ")
    print("Done.")

    print("Concatenating and saving out...")
    all_hw_ds_ensemble = xarray.concat(all_hw_ds, dim="member")
    xaer_hw_ds_ensemble = xarray.concat(xaer_hw_ds, dim="member")
    xghg_hw_ds_ensemble = xarray.concat(xghg_hw_ds, dim="member")

    all_hw_ds_ensemble.chunk(dict(member=1, year=-1, lat=96, lon=72)).to_zarr(f"{OUTPUT_DIR}CESM1_LE_all_TREFHTMN_HW_METRICS.zarr", consolidated=True)
    xaer_hw_ds_ensemble.chunk(dict(member=1, year=-1, lat=96, lon=72)).to_zarr(f"{OUTPUT_DIR}CESM1_LE_xaer_TREFHTMN_HW_METRICS.zarr", consolidated=True)
    xghg_hw_ds_ensemble.chunk(dict(member=1, year=-1, lat=96, lon=72)).to_zarr(f"{OUTPUT_DIR}CESM1_LE_xghg_TREFHTMN_HW_METRICS.zarr", consolidated=True)

    print("Computing metrics for MERRA2")
    INPUT_DIR = "/projects/dgs/persad_research/SIMULATION_DATA/ZARR/MERRA2/SIM_VARIABLES/"
    OUTPUT_DIR = "/projects/dgs/persad_research/SIMULATION_DATA/ZARR/MERRA2/HEAT_OUTPUTS/"

    tmin_merra2_ds = xarray.open_zarr(f"{INPUT_DIR}MERRA2_day_T2MMIN.zarr")["T2MMIN"]

    time_cftime = []
    days_to_drop = np.zeros(tmin_merra2_ds.time.size, dtype=bool)
    for index, date in enumerate(tmin_merra2_ds.time.values):
        year, month, day_stuff = str(date).split("-")
        day, hour_stuff = day_stuff.split("T")
        hour = hour_stuff.split(":")[0]
        try:
            timestamp = cftime.datetime(int(year), int(month), int(day), int(hour), calendar="noleap")
            time_cftime.append(timestamp)
        except ValueError:
            days_to_drop[index] = True

    calendar_mask = xarray.DataArray(
        data=days_to_drop,
        coords=dict(time=tmin_merra2_ds.time.values)
    )

    tmin_merra2_regrid = tmin_merra2_ds.interp(dict(lat=tmin_threshold.lat, lon=tmin_threshold.lon)).compute()
    tmin_merra2_regrid_time = tmin_merra2_regrid.where(calendar_mask - 1, drop=True).convert_calendar("noleap")

    merra2_hw_ds = hdp.compute_heatwave_metrics(tmin_merra2_regrid_time, tmin_threshold.sel(percentile=[0.9, 0.95], method="nearest"))
    merra2_hw_ds.to_zarr(f"{OUTPUT_DIR}MERRA2_T2MMIN_HW_METRICS.zarr")