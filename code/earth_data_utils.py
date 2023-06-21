
import os

# Suppress warnings
import warnings
warnings.simplefilter('ignore')
warnings.filterwarnings('ignore')

# Direct access
import earthaccess 
from pprint import pprint
import xarray as xr

# Harmony
import geopandas as gpd
import geoviews as gv
gv.extension('bokeh', 'matplotlib')
from harmony import BBox, Client, Collection, Request, LinkType
import datetime as dt
import s3fs
import matplotlib.pyplot as plt
import requests
import uuid


geojson_url = 'https://raw.githubusercontent.com/earth-artificial-intelligence/earth_data_cloud_clinic_geoweaver/main/gulf.json'


ssh_short_name = "SEA_SURFACE_HEIGHT_ALT_GRIDS_L4_2SATS_5DAY_6THDEG_V_JPL2205"
sst_short_name="MUR-JPL-L4-GLOB-v4.1"


def get_harmony_client():
  print("creating harmony client")
  harmony_client = Client()
  return harmony_client

def get_home_dir():
  home_dir = os.path.expanduser("~")
  return home_dir

def download_geojson(geojson_url):
  print("geojson_url: ", geojson_url)
  geojson_path = os.path.join(get_home_dir(), 'gulf.json')
  
  response = requests.get(geojson_url)
  with open(geojson_path, 'w') as f:
    f.write(response.text)
    print("saved to ", geojson_path)
  return geojson_path

def auth_earthaccess():
  return earthaccess.login(strategy="netrc", persist=True)


def get_dataset(results):
  return xr.open_mfdataset(earthaccess.open(results))
  
def get_subset(ds, var_name, lat=slice(10.8, 40.9), lon=slice(234.5,260.5)):
  print(ds)
  return ds[var_name].sel(Latitude=lat, Longitude=lon)
  




