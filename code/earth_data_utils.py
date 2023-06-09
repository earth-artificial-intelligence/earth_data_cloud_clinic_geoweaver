


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
