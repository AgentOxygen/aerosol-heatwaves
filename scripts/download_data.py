#!/usr/bin/env python
"""
download_data.py

Python script for computing the relevant heatwave thresholds for this particular study of LENS data.
"""
import hashlib
import urllib.request
import shutil
import os
from os.path import isdir, isfile
from urllib.parse import urlparse
import sys
import paths

API_KEY = ""

if __name__ == '__main__':
    API_KEY = sys.argv[1]
    
    for tref in ["TREFHTMN", "TREFHTMX"]:
        path_and_urls = [(paths.ALL_TREFHTMN_DATA, all_urls), (paths.XAER_TREFHTMN_DATA, xaer_urls)]
        if tref == "TREFHTMX": path_and_urls = [(paths.ALL_TREFHTMX_DATA, all_urls), (paths.XAER_TREFHTMX_DATA, xaer_urls)]
        
        for out_path, urls in path_and_urls:
            out_path = out_path + "DOWNLOAD/"
            print(f"Downloading {tref} files...")
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
                if not isfile(file_path):
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