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
start_date = "2022-05-28"
end_date = "2022-09-28"

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
)

items = search.item_collection()
print(f"Returned {len(items)} Items")


import datetime
selected_item = None
target_date = datetime.date(2022, 7, 21)
#try_2
for item in items:
    a_date = item.datetime.date()
    if a_date == target_date:
        selected_item = item
        break

if selected_item is not None:
    print(f"Processing: {selected_item.id}")
    # Access the VH (Vertical Transmit, Horizontal Receive)
    asset = selected_item.assets["vh"]
    signed_asset = sign(asset)

    # Read the data
    with rasterio.open(signed_asset.href) as src:
        data = src.read()

    # Calculate the mean backscatter coefficient
    mean_backscatter_coefficient = np.mean(data)
    #calculate 
    sigma0_data = 10 * np.log10(data.astype(np.float32) ** 2)
    print(f"Mean backscatter coefficient: {mean_backscatter_coefficient:.4f}")
    print(f"backscatter coefficients (sigma0): {sigma0_data:.4f}")

else:
    print("No Sentinel-1 data found for the specified date.")


"""
check available data->
for item in items:
    print(item.datetime.date())
"""
