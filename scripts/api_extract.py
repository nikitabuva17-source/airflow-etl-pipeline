import requests
import json

url = "https://randomuser.me/api/"

response = requests.get(url)
data = response.json()

with open("/opt/airflow/data_lake/raw_user.json", "w") as f:
    json.dump(data, f)

print("API data extracted")