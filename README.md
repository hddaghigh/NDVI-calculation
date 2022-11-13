# NDVI calculation and visualization

A simple python script for calculating NDVI values from earth observation multispectral data. Rasterio and numpy libraries are required.

## Installation

Clone the repository and install the required libraries using ```pip```:

```bash
git clone https://github.com/hamidubc/NDVI_calculation.git
cd NDVI/
pip install -r requirements.txt
```

## Examples

```bash

import numpy as np
import rasterio


filepath = 'https://hello.planet.com/data/s/L6GYNf4N6wTRydD/download/20210827_162545_60_2262_3B_AnalyticMS_8b.tif'

# read and exploring the data

with rasterio.open(filepath) as src:
  print(src.profile)
  print("Bands are: ", src.descriptions)
  redband = src.read([6]).astype('float64')
  nirband  = src.read([8]).astype('float64')

def calc_ndvi(nirband,redband):
    '''Calculate NDVI from integer arrays'''
    nirband = nirband.astype('float64')
    redband = redband.astype('float64')
    #ndvi = (nir - red) / (nir + red)
    ndvi = np.where((nirband + redband)==0.,0, (nirband-redband)/(nirband+redband))
    return ndvi

# test the output for the function defined
ndvi = calc_ndvi(nirband,redband)
 
example:
```
python main.py --url google.com --constant 5
```
