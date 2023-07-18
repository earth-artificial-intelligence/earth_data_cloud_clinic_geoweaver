from earth_data_utils import *

def search_and_get_sst():
  auth_earthaccess()
  results = earthaccess.search_data(
      short_name=sst_short_name,
      cloud_hosted=True,
      temporal=("2021-07-01", "2021-07-02"),
  )
  print("found results: ", results)
  return results

def plot_subset(ds_subset):
  ds_subset.plot(figsize=(12,6), x='lon', y='lat')
  home_dir = os.path.expanduser('~')
  
  file_name = f"geoweaver_plot_sst.png"
  save_file_path = os.path.join(home_dir, file_name)
  plt.savefig(save_file_path)
  print(f"new figure is saved to {save_file_path}")

with get_dataset(search_and_get_sst()) as ds:
  subset = ds["analysed_sst"].sel(lat=slice(37, 47), 
                                lon=slice(-70,-50)).std('time')
  plot_subset(subset)


