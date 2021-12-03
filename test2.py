import requests
import json

BASE = "https://elemental-leaf-332802.wl.r.appspot.com/WebScrapingAPI/"

response = requests.get(BASE + 'tableName/abc123')
print(response.json())

print(response.json()['1'])
