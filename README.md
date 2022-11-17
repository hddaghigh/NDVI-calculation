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
To create a virtual environment in the virtual_env folder:
```bash

python main.py --url https://hello.planet.com/data/s/L6GYNf4N6wTRydD/download/20210827_162545_60_2262_3B_AnalyticMS_8b.tif --ndviValue 0
```
