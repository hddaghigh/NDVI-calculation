# NDVI calculation and visualization

A simple python script for calculating The normalized difference vegetation index (NDVI) values from earth observation multispectral data. NDVI is an indicator of vegetation health based on how plants reflect certain ranges of the electromagnetic spectrum. 

## Set up new virtual environment
To create a virtual environment:

```bash
$ python3 -m venv venv

```

## Installation

Clone the repository and install the required libraries using ```pip```:

```bash
git clone https://github.com/hamidubc/NDVI_calculation.git
cd NDVI/
pip install -r requirements.txt
```

## Examples
Use the following command to run the code. The numeric value written after ndviThresh shows the results for that NDVI threshold.

```bash

python main.py --url https://hello.planet.com/data/s/L6GYNf4N6wTRydD/download/20210827_162545_60_2262_3B_AnalyticMS_8b.tif --ndviThresh 0

```
## Example

![Alt text](ndvi-image_withScale.jpg)
