from earth_data_utils import *

ssh_short_name = "SEA_SURFACE_HEIGHT_ALT_GRIDS_L4_2SATS_5DAY_6THDEG_V_JPL2205"

results = earthaccess.search_data(
    short_name=ssh_short_name,
    cloud_hosted=True,
    temporal=("2021-07-01", "2021-09-30"),
)
