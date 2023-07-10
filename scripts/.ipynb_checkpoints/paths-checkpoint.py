#!/usr/bin/env python
"""
paths.py

Centralized point for all file and data directory paths.
Contains unit tests for ensuring data structure integrity.
"""

import unittest
from os.path import isdir, isfile
from os import listdir


################# INPUT DATA PATHS #################
HEAD_DATA_DIR = "/projects/dgs/persad_research/heat_research/data/"

ALL_TREFHTMN_DATA = HEAD_DATA_DIR + "TREFHTMN/ALL/concatenated/"
XAER_TREFHTMN_DATA = HEAD_DATA_DIR + "TREFHTMN/XAER/concatenated/"
CONTROL_TREFHTMN_NETCDF = HEAD_DATA_DIR + "TREFHTMN/CONTROL/download/b.e11.B1850C5CN.f09_g16.005.cam.h1.TREFHTMN.19000101-19991231.nc"

ALL_TREFHTMX_DATA = HEAD_DATA_DIR + "TREFHTMX/ALL/concatenated/"
XAER_TREFHTMX_DATA = HEAD_DATA_DIR + "TREFHTMX/XAER/concatenated/"
CONTROL_TREFHTMX_NETCDF = HEAD_DATA_DIR + "TREFHTMX/CONTROL/download/b.e11.B1850C5CN.f09_g16.005.cam.h1.TREFHTMX.19000101-19991231.nc"

MERRA2_T2M_NETCDF = HEAD_DATA_DIR + "MERRA2/downloads/MERRA2_1980-2015.nc"
POPULATION_TIF = HEAD_DATA_DIR + "population/ppp_2020_1km_Aggregated.tif"

LANDMASK_NETCDF = HEAD_DATA_DIR + "land_mask.nc"

ALL_AODVIS_DATA = HEAD_DATA_DIR + "AODVIS/ALL/concatenated/"
XAER_AODVIS_DATA = HEAD_DATA_DIR + "AODVIS/XAER/concatenated/"


################# OUTPUT DATA PATHS #################
HEAD_OUTPUT_DIR = "/projects/dgs/persad_research/heat_research/output/"

ALL_THRESHOLDS = HEAD_OUTPUT_DIR + "thresholds/ALL/"
XAER_THRESHOLDS = HEAD_OUTPUT_DIR + "thresholds/XAER/"
CONTROL_TREFHTMN_THRESHOLD_NETCDF = HEAD_OUTPUT_DIR + "thresholds/CONTROL/control_trefhtmn_threshold.nc"
CONTROL_TREFHTMX_THRESHOLD_NETCDF = HEAD_OUTPUT_DIR + "thresholds/CONTROL/control_trefhtmx_threshold.nc"

ALL_TREFHTMN_HEAT_METRICS = HEAD_OUTPUT_DIR + "heat_metrics/TREFHTMN/ALL/"
XAER_TREFHTMN_HEAT_METRICS = HEAD_OUTPUT_DIR + "heat_metrics/TREFHTMN/XAER/"
CONTROL_TREFHTMN_HEAT_METRIC_NETCDF = HEAD_OUTPUT_DIR + "heat_metrics/TREFHTMN/CONTROL/control_trefhtmn.nc"

ALL_TREFHTMX_HEAT_METRICS = HEAD_OUTPUT_DIR + "heat_metrics/TREFHTMX/ALL/"
XAER_TREFHTMX_HEAT_METRICS = HEAD_OUTPUT_DIR + "heat_metrics/TREFHTMX/XAER/"
CONTROL_TREFHTMX_HEAT_METRIC_NETCDF = HEAD_OUTPUT_DIR + "heat_metrics/TREFHTMX/CONTROL/control_trefhtmx.nc"


class TestInputPaths(unittest.TestCase):
    
    def test_head_data_directory(self):
        # Test that it is indeed a directory
        self.assertTrue(isdir(HEAD_DATA_DIR))
        # Test that the path string includes a forward slash at the end
        self.assertEqual(HEAD_DATA_DIR[-1], "/")
    
    def test_all_trefhtmn_directory(self):
        # Test that it is indeed a directory
        self.assertTrue(isdir(ALL_TREFHTMN_DATA))
        # Test that the path string includes a forward slash at the end
        self.assertEqual(ALL_TREFHTMN_DATA[-1], "/")
        # Make sure all ensemble members are present
        self.assertEqual(len([name for name in listdir(ALL_TREFHTMN_DATA) if ".nc" in name]), 20)
    
    def test_xaer_trefhtmn_directory(self):
        # Test that it is indeed a directory
        self.assertTrue(isdir(XAER_TREFHTMN_DATA))
        # Test that the path string includes a forward slash at the end
        self.assertEqual(XAER_TREFHTMN_DATA[-1], "/")
        # Make sure all ensemble members are present
        self.assertEqual(len([name for name in listdir(XAER_TREFHTMN_DATA) if ".nc" in name]), 20)
                        
    def test_control_trefhtmn_directory(self):
        # Test that it is indeed a file
        self.assertTrue(isfile(CONTROL_TREFHTMN_NETCDF))
        # Make sure that it is a netCDF file
        extension = CONTROL_TREFHTMN_NETCDF.split(".")[-1]
        self.assertIn(extension, ["nc", "nc4"])
                         
    def test_all_trefhtmx_directory(self):
        # Test that it is indeed a directory
        self.assertTrue(isdir(ALL_TREFHTMX_DATA))
        # Test that the path string includes a forward slash at the end
        self.assertEqual(ALL_TREFHTMX_DATA[-1], "/")
        # Make sure all ensemble members are present
        self.assertEqual(len([name for name in listdir(ALL_TREFHTMX_DATA) if ".nc" in name]), 20)
    
    def test_xaer_trefhtmx_directory(self):
        # Test that it is indeed a directory
        self.assertTrue(isdir(XAER_TREFHTMX_DATA))
        # Test that the path string includes a forward slash at the end
        self.assertEqual(XAER_TREFHTMX_DATA[-1], "/")
        # Make sure all ensemble members are present
        self.assertEqual(len([name for name in listdir(XAER_TREFHTMX_DATA) if ".nc" in name]), 20)
                        
    def test_control_trefhtmx_netcdf(self):
        # Test that it is indeed a file
        self.assertTrue(isfile(CONTROL_TREFHTMX_NETCDF))
        # Make sure that it is a netCDF file
        extension = CONTROL_TREFHTMX_NETCDF.split(".")[-1]
        self.assertIn(extension, ["nc", "nc4"])
                         
    def test_merra2_t2m_netcdf(self):
        # Test that it is indeed a file
        self.assertTrue(isfile(MERRA2_T2M_NETCDF))
        # Make sure that it is a netCDF file
        extension = MERRA2_T2M_NETCDF.split(".")[-1]
        self.assertIn(extension, ["nc", "nc4"])
                         
    def test_population_tif(self):
        # Test that it is indeed a file
        self.assertTrue(isfile(POPULATION_TIF))
        # Make sure that it is a TIF file
        extension = POPULATION_TIF.split(".")[-1]
        self.assertEqual(extension, "tif")
        
    def test_landmask_netcdf(self):
        # Test that it is indeed a file
        self.assertTrue(isfile(LANDMASK_NETCDF))
        # Make sure that it is a netCDF file
        extension = LANDMASK_NETCDF.split(".")[-1]
        self.assertIn(extension, ["nc", "nc4"])

    def test_all_aodvis_directory(self):
        # Test that it is indeed a directory
        self.assertTrue(isdir(ALL_AODVIS_DATA))
        # Test that the path string includes a forward slash at the end
        self.assertEqual(ALL_AODVIS_DATA[-1], "/")
        # Make sure all ensemble members are present
        self.assertEqual(len([name for name in listdir(ALL_AODVIS_DATA) if ".nc" in name]), 20)
        
    def test_xaer_aodvis_directory(self):
        # Test that it is indeed a directory
        self.assertTrue(isdir(XAER_AODVIS_DATA))
        # Test that the path string includes a forward slash at the end
        self.assertEqual(XAER_AODVIS_DATA[-1], "/")
        # Make sure all ensemble members are present
        self.assertEqual(len([name for name in listdir(XAER_AODVIS_DATA) if ".nc" in name]), 20)


class TestOutputPaths(unittest.TestCase):
    
    def test_head_output_directory(self):
        # Test that it is indeed a directory
        self.assertTrue(isdir(HEAD_OUTPUT_DIR))
        # Test that the path string includes a forward slash at the end
        self.assertEqual(HEAD_OUTPUT_DIR[-1], "/")
        
    def test_all_trefhtmn_heat_directory(self):
        # Test that it is indeed a directory
        self.assertTrue(isdir(ALL_TREFHTMN_HEAT_METRICS))
        # Test that the path string includes a forward slash at the end
        self.assertEqual(ALL_TREFHTMN_HEAT_METRICS[-1], "/")
        # Make sure all ensemble members are present
        self.assertEqual(len([name for name in listdir(ALL_TREFHTMN_HEAT_METRICS) if ".nc" in name]), 20)
        
    def test_xaer_trefhtmn_heat_directory(self):
        # Test that it is indeed a directory
        self.assertTrue(isdir(XAER_TREFHTMN_HEAT_METRICS))
        # Test that the path string includes a forward slash at the end
        self.assertEqual(XAER_TREFHTMN_HEAT_METRICS[-1], "/")
        # Make sure all ensemble members are present
        self.assertEqual(len([name for name in listdir(XAER_TREFHTMN_HEAT_METRICS) if ".nc" in name]), 20)
        
    def test_control_trefhtmn_heat_netcdf(self):
        # Test that it is indeed a file
        self.assertTrue(isfile(CONTROL_TREFHTMN_HEAT_METRIC_NETCDF))
        # Make sure that it is a netCDF file
        extension = CONTROL_TREFHTMN_HEAT_METRIC_NETCDF.split(".")[-1]
        self.assertIn(extension, ["nc", "nc4"])
        
    def test_all_trefhtmx_heat_directory(self):
        # Test that it is indeed a directory
        self.assertTrue(isdir(ALL_TREFHTMX_HEAT_METRICS))
        # Test that the path string includes a forward slash at the end
        self.assertEqual(ALL_TREFHTMX_HEAT_METRICS[-1], "/")
        # Make sure all ensemble members are present
        self.assertEqual(len([name for name in listdir(ALL_TREFHTMX_HEAT_METRICS) if ".nc" in name]), 20)
        
    def test_xaer_trefhtmx_heat_directory(self):
        # Test that it is indeed a directory
        self.assertTrue(isdir(XAER_TREFHTMX_HEAT_METRICS))
        # Test that the path string includes a forward slash at the end
        self.assertEqual(XAER_TREFHTMX_HEAT_METRICS[-1], "/")
        # Make sure all ensemble members are present
        self.assertEqual(len([name for name in listdir(XAER_TREFHTMX_HEAT_METRICS) if ".nc" in name]), 20)
        
    def test_control_trefhtmx_heat_netcdf(self):
        # Test that it is indeed a file
        self.assertTrue(isfile(CONTROL_TREFHTMX_HEAT_METRIC_NETCDF))
        # Make sure that it is a netCDF file
        extension = CONTROL_TREFHTMX_HEAT_METRIC_NETCDF.split(".")[-1]
        self.assertIn(extension, ["nc", "nc4"])


if __name__ == '__main__':
    unittest.main()
