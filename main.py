"""
Author: anlt
File: Main.py
"""

import requests

URL = 'https://api.tdameritrade.com/v1/instruments'

payload = {'apikey': '4R1O5OSYDJALDKV8FTBP9EYCKQJUTBPX',
           'symbol': 'GOOG',
           'projection': 'fundamental'}

result = requests.get(URL, params=payload)

print(result.json())