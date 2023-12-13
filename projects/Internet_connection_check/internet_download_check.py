# Method 1: using speedtest module
import speedtest

#creates an instance of the Speedtest class
#interact with the speedtest module and perform measurements
st = speedtest.Speedtest()
#retrieves information about available speedtest servers 
#chooses the one that is considered to be the "best" for the current location based on factors like ping and latency
best_server = st.get_best_server()

print(f"Testing download speed from server {best_server['host']}...")
#initiates a download test from the chosen server and measures the download speed
#bytes per second
download_speed = st.download()

#divides download speed in bytes per second by 1024**2 to convert it to megabits per second (Mbps)
# 1 byte = 8 bits - not sure if need to divide by 8 as well
# 1 kilobyte = 1024 bytes
# 1 megabit = 1024 bits
print(f"Download Speed: {download_speed / (1024**2):.2f} Mbps")


# ----------------------------------------------------------------------------------------
# Method 2: manual calculation
# import requests
# from time import time
# from requests.exceptions import ConnectionError

# def download_speed_test(url='https://datacatalogfiles.worldbank.org/ddh-published/0061111/DR0085897/02--CHAPTER%202.rar?versionId=2023-01-18T19:02:19.7709485Z'):
#   """
#   Tests the download speed of the given URL.

#   Args:
#     url: The URL to download the data from.

#   Returns:
#     A tuple containing the download speed in megabits per second (Mbps) and the response status code.
#   """
#   #save current time as reference point
#   start_time = time() 

#   try:
#     #sends a GET req to the URL, download data in chunks, time out 5s
#     response = requests.get(url, stream=True, timeout=5) 
#     #get content length from service resp header, if none, set to 0
#     content_length = int(response.headers.get('content-length', 0))

#     if content_length > 0:
#       #keep track of bytes downloaded
#       downloaded_bytes = 0
#       # iterate over downloaded data in chunks of 1024 bytes
#       # 1024 bytes: compatability (Many network protocols and libraries are designed to work with data chunks of specific sizes.)
#       for chunk in response.iter_content(chunk_size=1024):
#         #update downloaded_bytes counter
#         downloaded_bytes += len(chunk)
#       #calculate download time from current time - start time
#       download_time = time() - start_time
#       print(download_time)

#       # Convert bytes to megabits (Mb) and calculate speed in Mbps
#       # downloaded_bytes * 8: bytes to bits (1 byte = 8 bits)
#       # download_time * 1024 * 1024: 
#       download_speed = (downloaded_bytes * 8) / (download_time * 1024 * 1024)
#       return download_speed, response.status_code
#     else:
#       print(f'Failed to determine content length for {url}.')
#       return 0, response.status_code
#   except ConnectionError as e:
#     print(f'Failed to connect to {url}.')
#     return 0, None
#   except Exception as e:
#     print(f'Error while testing download speed: {e}')
#     return 0, None

# # Get download speed and status code
# download_speed, status_code = download_speed_test()
# ### From Wayne: Can use a bigger file size for speed test as your current file is too small
# # url='https://link.testfile.org/150MB' 

# if download_speed > 0:
#   print(f'Download speed: {download_speed:.2f} Mbps')
# else:
#   print(f'Failed to measure download speed.')

# if status_code:
#   print(f'Status code: {status_code}')


