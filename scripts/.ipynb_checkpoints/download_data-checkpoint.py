#!/usr/bin/env python
"""
download_data.py

Python script for computing the relevant heatwave thresholds for this particular study of LENS data.
"""


#!/usr/bin/env python3

import hashlib
import urllib.request
import shutil
import os
from os.path import isdir
from urllib.parse import urlparse
import sys
import paths

API_KEY = ""

if __name__ == '__main__':
    API_KEY = sys.argv[1]
    
    all_urls = [
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRC5CNBDRD.f09_g16.001.cam.h1.TREFHTMN.18500101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRC5CNBDRD.f09_g16.002.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRC5CNBDRD.f09_g16.003.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRC5CNBDRD.f09_g16.004.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRC5CNBDRD.f09_g16.005.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRC5CNBDRD.f09_g16.006.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRC5CNBDRD.f09_g16.007.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRC5CNBDRD.f09_g16.008.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRC5CNBDRD.f09_g16.009.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRC5CNBDRD.f09_g16.010.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRC5CNBDRD.f09_g16.011.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRC5CNBDRD.f09_g16.012.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRC5CNBDRD.f09_g16.013.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRC5CNBDRD.f09_g16.014.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRC5CNBDRD.f09_g16.015.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRC5CNBDRD.f09_g16.016.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRC5CNBDRD.f09_g16.017.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRC5CNBDRD.f09_g16.018.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRC5CNBDRD.f09_g16.019.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRC5CNBDRD.f09_g16.020.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.001.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.001.cam.h1.TREFHTMN.20810101-21001231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.002.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.002.cam.h1.TREFHTMN.20810101-21001231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.003.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.003.cam.h1.TREFHTMN.20810101-21001231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.004.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.004.cam.h1.TREFHTMN.20810101-21001231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.005.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.005.cam.h1.TREFHTMN.20810101-21001231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.006.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.006.cam.h1.TREFHTMN.20810101-21001231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.007.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.007.cam.h1.TREFHTMN.20810101-21001231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.008.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.008.cam.h1.TREFHTMN.20810101-21001231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.009.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.009.cam.h1.TREFHTMN.20810101-21001231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.010.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.010.cam.h1.TREFHTMN.20810101-21001231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.011.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.011.cam.h1.TREFHTMN.20810101-21001231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.012.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.012.cam.h1.TREFHTMN.20810101-21001231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.013.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.013.cam.h1.TREFHTMN.20810101-21001231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.014.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.014.cam.h1.TREFHTMN.20810101-21001231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.015.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.015.cam.h1.TREFHTMN.20810101-21001231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.016.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.016.cam.h1.TREFHTMN.20810101-21001231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.017.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.017.cam.h1.TREFHTMN.20810101-21001231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.018.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.018.cam.h1.TREFHTMN.20810101-21001231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.019.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.019.cam.h1.TREFHTMN.20810101-21001231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.020.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.BRCP85C5CNBDRD.f09_g16.020.cam.h1.TREFHTMN.20810101-21001231.nc?api-token={API_KEY}"]

    xaer_urls = [
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.001.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.001.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.002.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.002.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.003.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.003.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.004.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.004.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.005.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.005.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.006.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.006.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.007.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.007.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.008.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.008.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.009.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.009.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.010.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.010.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.011.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.011.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.012.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.012.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.013.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.013.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.014.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.014.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.015.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.015.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.016.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.016.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.017.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.017.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.018.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.018.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.019.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.019.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.020.cam.h1.TREFHTMN.19200101-20051231.nc?api-token={API_KEY}",
         f"https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cesm/collections/cesmLE/CESM-CAM5-BGC-LE/atm/proc/tseries/daily/TREFHTMN/b.e11.B20TRLENS_RCP85.f09_g16.xaer.020.cam.h1.TREFHTMN.20060101-20801231.nc?api-token={API_KEY}"]

    for out_path, urls in [(paths.ALL_TREFHTMN_DATA, all_urls), (paths.XAER_TREFHTMN_DATA, xaer_urls)]:
        if not isdir(out_path):
            os.makedirs(out_path)
        
        # Gets filename even when there are parameters (but uses urlparse and os)
        def get_filename(url):
            a = urlparse(url)
            return os.path.basename(a.path)

        opener = urllib.request.build_opener()
        # opener.addheaders = [("User-agent", PYTHON_USER_AGENT)]
        # opener.addheaders.append(("Authorization", "api-token {}".format(API_KEY)))

        for url in urls:
            file_path = out_path + get_filename(url)

            print("Downloading File: ", url)

            try:
                with opener.open(url) as response, open(file_path, 'ab') as out_file:
                    shutil.copyfileobj(response, out_file)
            except urllib.error.HTTPError as e:
            # Return code error (e.g. 404, 501, ...)
                print("HTTPError: {}".format(e.code))
            except urllib.error.URLError as e:
            # Not an HTTP-specific error (e.g. connection refused)
                print("URLError: {}".format(e.reason))
            else:
                # 200
                print("Success")