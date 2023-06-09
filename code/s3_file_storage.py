import matplotlib.pyplot as plt
from earth_access_authenticate import *

try:
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
  plt.savefig('plot.png')
except Exception as e:
  print('please check the write permissions to directory', e)
