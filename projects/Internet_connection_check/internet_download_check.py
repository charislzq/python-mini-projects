import requests
from time import time
from requests.exceptions import ConnectionError

def download_speed_test(url='https://datacatalogfiles.worldbank.org/ddh-published/0061111/DR0085897/02--CHAPTER%202.rar?versionId=2023-01-18T19:02:19.7709485Z'):
  """
  Tests the download speed of the given URL.

  Args:
    url: The URL to download the data from.

  Returns:
    A tuple containing the download speed in megabits per second (Mbps) and the response status code.
  """
  start_time = time()

  try:
    response = requests.get(url, stream=True, timeout=5)
    content_length = int(response.headers.get('content-length', 0))

    if content_length > 0:
      downloaded_bytes = 0
      for chunk in response.iter_content(chunk_size=1024):
        downloaded_bytes += len(chunk)
      download_time = time() - start_time

      # Convert bytes to megabits and calculate speed
      download_speed = (downloaded_bytes * 8) / (download_time * 1024 * 1024)
      return download_speed, response.status_code
    else:
      print(f'Failed to determine content length for {url}.')
      return 0, response.status_code
  except ConnectionError as e:
    print(f'Failed to connect to {url}.')
    return 0, None
  except Exception as e:
    print(f'Error while testing download speed: {e}')
    return 0, None

# Get download speed and status code
download_speed, status_code = download_speed_test()

if download_speed > 0:
  print(f'Download speed: {download_speed:.2f} Mbps')
else:
  print(f'Failed to measure download speed.')

if status_code:
  print(f'Status code: {status_code}')

