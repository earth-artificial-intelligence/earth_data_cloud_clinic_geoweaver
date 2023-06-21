from earth_data_utils import *

def search_ssh():
  auth_earthaccess()
  results = earthaccess.search_data(
      short_name=ssh_short_name,
      cloud_hosted=True,
      temporal=("2021-07-01", "2021-09-30"),
  )
  return results

def plot_subset(ds_subset):
  ds_subset.plot(figsize=(12,6), x='Longitude', y='Latitude')
  home_dir = os.path.expanduser('~')
  
  file_name = f"geoweaver_plot_ssh.png"
  save_file_path = os.path.join(home_dir, file_name)
  plt.savefig(save_file_path)
  print(f"new figure is saved to {save_file_path}")

with get_dataset(search_ssh()) as ds:
  subset = ds["SLA"].sel(Latitude=slice(-79, 79), 
                       Longitude=slice(100,300)).std('Time')
  plot_subset(subset)

