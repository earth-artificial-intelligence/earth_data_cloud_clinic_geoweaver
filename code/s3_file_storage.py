# Suppress warnings
import os
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
from earth_access_authenticate import *

creds = harmony_client.aws_credentials()
s3_fs = s3fs.S3FileSystem(
  key=creds['aws_access_key_id'],
  secret=creds['aws_secret_access_key'],
  token=creds['aws_session_token'],
  client_kwargs={'region_name':'us-west-2'},
)
f = s3_fs.open(url, mode='rb')
ds = xr.open_dataset(f)
ds.analysed_sst.plot()
home_dir = os.path.expanduser('~')
plt.savefig(os.path.join(home_dir, 'plot2.png'))
