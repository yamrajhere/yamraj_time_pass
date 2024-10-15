import requests
import json
import proxies_add
import profile_ids

url = "http://localhost:8848/api/agent/profile/proxy/batch"
api_key = "d7408bb8-7aa3-44c8-baf1-5cdcb1bba371"

for items in profile_ids.all_profile_ids:

   payload = json.dumps({
      "profileIds": [
         f"{items}"
      ],
      "proxyConfig": {
         "host": f"{proxies_add.host_proxy}",
         "password": f"{proxies_add.password_proxy}",
         "port": f"{proxies_add.port_proxy}",
         "proxyType": f"{proxies_add.mode_proxy}",
         "username": f"{proxies_add.username_proxy}"
      }
   })
   headers = {
      "x-api-key" : api_key,
      'User-Agent': 'Apidog/1.0.0 (https://apidog.com)',
      'Content-Type': 'application/json'
   }

   response = requests.request("PUT", url, headers=headers, data=payload)
   print(response.text)