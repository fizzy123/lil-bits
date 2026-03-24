import requests
import redis

links = []
channels = [
  "readitlater-cgomtuzwqx0",
  "feeds-qpff57zh3xi",
  "repeats-buiaytfetsk",
]
for channel in channels:
  res = requests.get(f"https://api.are.na/v2/channels/{channel}/contents?page=1&per=10000", headers={"User-Agent":"Python"})
  for link in res.json()["contents"]:
    links.append(link["source"]["url"])

r = redis.Redis(host='redis')
r.set("feed", " ".join(links))
