from dotenv import load_dotenv
import requests, json, time, os

load_dotenv()

api_key = os.getenv("football_data_api_key")

matches_url = "https://api.football-data.org/v4/competitions/PL/matches"
headers = {"X-Auth-Token": api_key}

os.makedirs("data/raw", exist_ok=True)

for season in [2023, 2024, 2025]:
    path = f"data/raw/matches_{season}.json"
    if os.path.exists(path):          
        continue
    r = requests.get(matches_url, headers=headers, params={"season": season})
    print(season, r.status_code)
    r.raise_for_status()
    with open(path, "w") as f:
        json.dump(r.json(), f)
    time.sleep(7) 

matches_url = "https://api.football-data.org/v4/competitions/PL/matches"
headers = {"X-Auth-Token": api_key}

os.makedirs("data/raw", exist_ok=True)

path = "data/raw/matches_2026.json"
r = requests.get(matches_url, headers=headers)
print(path, r.status_code)
r.raise_for_status()
with open(path, "w") as f:
    json.dump(r.json(), f)


standings_url = "https://api.football-data.org/v4/competitions/PL/standings"
headers = {"X-Auth-Token": api_key}

os.makedirs("data/raw", exist_ok=True)

path = "data/raw/standings.json"
r = requests.get(standings_url, headers=headers)
print(path, r.status_code)
r.raise_for_status()
with open(path, "w") as f:
    json.dump(r.json(), f, indent=2)