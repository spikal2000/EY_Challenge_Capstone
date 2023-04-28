# -*- coding: utf-8 -*-
"""
Capstone Project
"""
"""
installs:
pip install pandas
pip install pystac-client
pip install planetary-computer
pip install rasterio
    
"""
import os
import numpy as np
from planetary_computer import sign
import rasterio
import pystac_client
import planetary_computer

#API key
os.environ["PL_API_KEY"] = "63b9f723802a491391fbac613f954916"

#Search parametrs
latitude = 10.542192
longitude = 105.18792
start_date = "2021-01-01"
end_date = "2021-12-31"

#AOI
bbox = [longitude - 0.05, 
        latitude - 0.05, 
        longitude + 0.05, 
        latitude + 0.05]

#STAC API client
client = pystac_client.Client.open(
    "https://planetarycomputer.microsoft.com/api/stac/v1",
    modifier=planetary_computer.sign_inplace,
)

# Search for Sentinel-1 data
search = client.search(
    collections=["sentinel-1-grd"],
    bbox=bbox,
    datetime=f"{start_date}/{end_date}",
    limit=500, 
)

items = list(search.get_items())

print(f"Found {len(items)} items")

# Get data
for item in items:
    print(f"Processing: {item.id}")
    # Access the VH (Vertical Transmit, Horizontal Receive)
    asset = item.assets["vh"]
    signed_asset = sign(asset)
    # read the data ig
    with rasterio.open(signed_asset.href) as src:
        data = src.read()
        print(data)


