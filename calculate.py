# importing required libraries
import math
import rasterio
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import cv2
from functools import lru_cache

@lru_cache(maxsize=32)
def import_data(url):
  return rasterio.open(url)

def calculate(filepath, threshold=0):

  # opening the tiff file
  sat_data = import_data(filepath)
  width_in_projected_units = sat_data.bounds.right - sat_data.bounds.left
  height_in_projected_units = sat_data.bounds.top - sat_data.bounds.bottom
  print("Width: {}, Height: {}".format(width_in_projected_units, height_in_projected_units))

  #print the shape of data 
  sat_data.shape
  print(sat_data)

  #print the width and height
  print("Rows: {}, Columns: {}".format(sat_data.height, sat_data.width))
  row_min = 0
  col_min = 0
  row_max = sat_data.height - 1
  col_max = sat_data.width - 1
  topleft = sat_data.transform * (row_min, col_min)
  botright = sat_data.transform * (row_max, col_max)
  print("Top left corner coordinates: {}".format(topleft))
  print("Bottom right corner coordinates: {}".format(botright))

  # print the number of bands
  print(sat_data.count)

  #the indices will be 8 beacuse it has 8 dimeansions
  print(sat_data.indexes)

  
  with rasterio.open(filepath) as src: #reads red (6th) band
    band_red = src.read(6)
  with rasterio.open(filepath) as src: #reads nir (8th) band
    band_nir = src.read(8)

  np.seterr(divide='ignore',invalid='ignore')

  # claculate NDVI using ndvi_calculation function
  def ndvi_calculation(band_nir,band_red):
    ndvi = (band_nir.astype(float) - band_red.astype(float)) / (band_nir + band_red) # The Eq. for ndvi
    return ndvi

  # checking the output for the ndvi_calculation fuction 
  ndvi = ndvi_calculation(band_nir,band_red)

  print(np.nanmin(ndvi)) 
  print(np.nanmax(ndvi))

  meta = src.meta
  print(meta)


  ndvi_dtype = ndvi.dtype
  print(ndvi_dtype)


  kwargs = meta


  kwargs.update(dtype=ndvi_dtype)


  kwargs.update(count=1)


  with rasterio.open('Newimage.tif', 'w', **kwargs) as dst:
          dst.write(ndvi, 1)

  class MidpointNormalize(colors.Normalize):
    
      def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
          self.midpoint = midpoint
          colors.Normalize.__init__(self, vmin, vmax, clip)

      def __call__(self, value, clip=None):
        
          x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
          return np.ma.masked_array(np.interp(value, x, y), np.isnan(value))

  # Write it out to a GeoTIff file in a EPSG 4326 projection
  with rasterio.open(
          'Newimage.tif',
          'w',
          driver='GTiff',
          width=sat_data.width,
          height=sat_data.height,
          count=1,
          dtype= np.uint8,
          nodata=0,
          transform=sat_data.transform,
          crs={'init': 'EPSG:4326'}) as dst:
      dst.write(ndvi, 1)

  min=np.nanmin(ndvi)
  max=np.nanmax(ndvi)

  mid=0.1

  # Display NDVI through Red-Yellow-Blue color
  colormap = plt.cm.RdYlGn 
  norm = MidpointNormalize(vmin=min, vmax=max, midpoint=mid)
  fig = plt.figure(figsize=(20,10))

  ax = fig.add_subplot(111)
  cbar_plot = ax.imshow(ndvi, cmap=colormap, vmin=min, vmax=max, norm=norm)
  ax.axis('off')
  ax.set_title('NDVI Index', fontsize=17, fontweight='bold')

  cbar = fig.colorbar(cbar_plot, shrink=0.65)

  fig.savefig("ndvi-image.jpg", dpi=300, bbox_inches='tight', pad_inches=0.7)

  # display the image with NDVI values
  plt.show()

  fig2 = plt.figure(figsize=(20,10))
  ax = fig2.add_subplot(111)

  # display the Histogram for NDVI to explore pixel number vs. NDVI value
  plt.title("NDVI Histogram", fontsize=18, fontweight='bold')
  plt.xlabel("NDVI values", fontsize=14)
  plt.ylabel("Number of pixels", fontsize=14)



  x = ndvi[~np.isnan(ndvi)]
  color = 'g'
  ax.hist(x,bins=30,color=color,histtype='bar', ec='black')
  plt.show()

  min=np.nanmin(ndvi)
  max=np.nanmax(ndvi)

  mid=0.1

  colormap = plt.cm.RdYlGn 
  norm = MidpointNormalize(vmin=min, vmax=max, midpoint=mid)
  fig1 = plt.figure(figsize=(20,10))

  ax = fig1.add_subplot(111)
  cbar_plot = ax.imshow(ndvi, cmap=colormap, vmin=min, vmax=max, norm=norm)
  ax.axis('off')


  fig1.savefig("ndviresult.jpg", dpi=600, bbox_inches='tight', pad_inches=0.7)

  ndvi_min=np.nanmin(ndvi)
  ndvi_max=np.nanmax(ndvi)
  print(min)
  print(max)
  print('Min NDVI: %.3f, Max NDVI: %.3f' % (np.nanmin(ndvi), np.nanmax(ndvi)))
  ndvi_range = max -min
  print('ndvi_range:',ndvi_range)

