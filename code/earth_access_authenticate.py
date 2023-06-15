import os
import requests
from search_data import *
from harmony import BBox, Client, Collection, Request, LinkType
import datetime as dt
import s3fs
import matplotlib.pyplot as plt
from earth_access_authenticate import *
import earthaccess 
from pprint import pprint
import xarray as xr

# Harmony
import geopandas as gpd

ssh_short_name = "SEA_SURFACE_HEIGHT_ALT_GRIDS_L4_2SATS_5DAY_6THDEG_V_JPL2205"

results = earthaccess.search_data(
    short_name=ssh_short_name,
    cloud_hosted=True,
    temporal=("2021-07-01", "2021-09-30"),
)
sst_short_name="MUR-JPL-L4-GLOB-v4.1"

results = earthaccess.search_data(
    short_name=ssh_short_name,
    cloud_hosted=True,
    temporal=("2021-07-01", "2021-09-30"),
)

auth = earthaccess.login(strategy="netrc", persist=True)
ds = xr.open_mfdataset(earthaccess.open(results))
geojson_url = 'https://raw.githubusercontent.com/earth-artificial-intelligence/earth_data_cloud_clinic_geoweaver/main/gulf.json'

home_dir = os.path.expanduser('~')
geojson_path = os.path.join(home_dir, 'gulf.json')
response = requests.get(geojson_url)
with open(geojson_path, 'w') as f:
	f.write(response.text)

gdf = gpd.read_file(geojson_path) #Return a GeoDataFrame object


harmony_client = Client()
sst_short_name="MUR-JPL-L4-GLOB-v4.1"

request = Request(
  collection=Collection(id=sst_short_name),
  shape=geojson_path,
  temporal={
    'start': dt.datetime(2021, 8, 1, 1),
    'stop': dt.datetime(2021, 8, 1, 2)   
  },
)
job_id = harmony_client.submit(request)
harmony_client.wait_for_processing(job_id, show_progress=False)
data = harmony_client.result_json(job_id)
results = harmony_client.result_urls(job_id, link_type=LinkType.s3)
urls = list(results)
url = urls[0]


