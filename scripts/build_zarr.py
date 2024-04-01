#!/usr/bin/env python
"""
build_zarr.py

Generates zarr directories for use in project analysis. Zarr
allows for faster parallel computing than netCDF.

"""
import xarray
from distributed import Client
import cftime
import dask


if __name__ == '__main__':
    client = Client('localhost:8786')

    OUTPUT_DIR = "/projects/dgs/persad_research/SIMULATION_DATA/ZARR/LENS1/SIM_VARIABLES/"
    INPUT_DIR = "/projects/dgs/persad_research/SIMULATION_DATA/DATA/LENS1/CESM1/"

    start = cftime.DatetimeNoLeap(1920, 1, 1, 0, 0, 0, 0, has_year_zero=True)
    end = cftime.DatetimeNoLeap(2100, 12, 31, 0, 0, 0, 0, has_year_zero=True)

    for exp in ["all", "xaer", "xghg"]:
        for variable in ["TREFHTMN", "TREFHTMX"]:
            print(f"{exp} - {variable}")
            member_ds = []
            member_labels = []
            for i in range(1, 21):
                ts_ds = xarray.open_mfdataset(f"{INPUT_DIR}{exp}/{str(i).zfill(3)}/day/{variable}/*.nc", chunks=dict(time=-1, lat=-1, lon=-1))
                member_ds.append(ts_ds.sel(time=slice(start, end)))
                member_labels.append(str(i).zfill(3))
                print(i, end=", ")

            with dask.config.set(**{'array.slicing.split_large_chunks': False}):
                ensemble_ds = xarray.concat(member_ds, dim="member").assign_coords({"member": member_labels}).chunk(dict(time=-1, member=1, lat=96, lon=72))
            print("Saving out...")
            ensemble_ds.to_zarr(f"{OUTPUT_DIR}{exp}_day_{variable}.zarr", consolidated=True, mode="w")

    print("Loading preindustrial controls...")
    trefhtmn_pi = xarray.open_mfdataset(f"{INPUT_DIR}preindustrial/005/day/TREFHTMN/*.nc", chunks=dict(time=365*100, lat=-1, lon=-1)).chunk(dict(time=-1, lat=48, lon=36))
    trefhtmx_pi = xarray.open_mfdataset(f"{INPUT_DIR}preindustrial/005/day/TREFHTMX/*.nc", chunks=dict(time=365*100, lat=-1, lon=-1)).chunk(dict(time=-1, lat=48, lon=36))

    print("Saving out preindustrial controls...")
    trefhtmn_pi.to_zarr(f"{OUTPUT_DIR}preindustrial_day_TREFHTMN.zarr", consolidated=True, mode="w")
    trefhtmx_pi.to_zarr(f"{OUTPUT_DIR}preindustrial_day_TREFHTMX.zarr", consolidated=True, mode="w")

    print("Rechunking MERRA2...")
    merra2_ds = xarray.open_mfdataset("/projects/dgs/persad_research/SIMULATION_DATA/DATA/GES/MERRA2/statD/single-level/day/T2_PRECIP_DIAGNOSTICS/*")

    OUT_PATH = "/projects/dgs/persad_research/SIMULATION_DATA/ZARR/MERRA2/SIM_VARIABLES/"

    rechunked_ds = merra2_ds.chunk(dict(time=-1, lat=91, lon=144))

    print("Saving out MERRA2...")
    rechunked_ds[["HOURNORAIN"]].to_zarr(f"{OUT_PATH}MERRA2_day_HOURNORAIN.zarr", consolidated=True, mode="w")
    rechunked_ds[["T2MMAX"]].to_zarr(f"{OUT_PATH}MERRA2_day_T2MMAX.zarr", consolidated=True, mode="w")
    rechunked_ds[["T2MMEAN"]].to_zarr(f"{OUT_PATH}MERRA2_day_T2MMEAN.zarr", consolidated=True, mode="w")
    rechunked_ds[["T2MMIN"]].to_zarr(f"{OUT_PATH}MERRA2_day_T2MMIN.zarr", consolidated=True, mode="w")
    rechunked_ds[["TPRECMAX"]].to_zarr(f"{OUT_PATH}MERRA2_day_TPRECMAX.zarr", consolidated=True, mode="w")