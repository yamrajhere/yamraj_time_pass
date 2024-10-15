import requests
import json



url = "http://localhost:8848/api/agent/profile/list"

payload={}
headers = {
   "x-api-key" : "d7408bb8-7aa3-44c8-baf1-5cdcb1bba371",
   'User-Agent': 'Apidog/1.0.0 (https://apidog.com)'
}
response = requests.request("GET", url, headers=headers, data=payload)


data = json.loads(response.text)
profiles = data['data']['docs']
profile_ids = [profile['profileId'] for profile in profiles]

print(profile_ids)
with open("profile_ids.py", "w") as f:
    f.write(f"all_profile_ids = {profile_ids}")