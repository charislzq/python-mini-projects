import requests
from requests.exceptions import ConnectionError

# Cheng Yi's recommendation
import os
def internet_connection_test(url:str):
  print(f'Attempting to connect to {url} to determine internet connection status.')
  
  try:
    # ping uses ICMP protocol
  	# pinging with 5 packets via -c flag with 10 second timeout
   response = os.popen(f"ping -c 5 -t 10 {url}")
   for line in response.readlines():
      print(line)
  except:
    print(f"Failed with unparsed reason.")
    
  # uses HTTP protocol
	# try:
	# 	print(url)
	# 	resp = requests.get(url, timeout = 10)
	# 	resp.text
	# 	resp.status_code
	# 	print(f'Connection to {url} was successful.')
	# 	return True
	# except ConnectionError as e:
	# 	requests.ConnectionError
	# 	print(f'Failed to connect to {url}.')
	# 	return False
	# except:
	# 	print(f'Failed with unparsed reason.')
	# 	return False

def internet_connection_test():
	url = 'https://www.google.com/'
	# url = 'https://github.com/Python-World/python-mini-projects/tree/master/projects/Internet_connection_check'
	print(f'Attempting to connect to {url} to determine internet connection status.')
	
	try:
		print(url)
		resp = requests.get(url, timeout = 10)
		resp.text
		resp.status_code
		print(f'Connection to {url} was successful.')
		return True
	except ConnectionError as e:
		requests.ConnectionError
		print(f'Failed to connect to {url}.')
		return False
	except:
		print(f'Failed with unparsed reason.')
		return False

internet_connection_test()
