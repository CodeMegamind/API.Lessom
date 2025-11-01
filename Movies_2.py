import requests


Cyberpunk = {
  "title": "CyberPunk",
  "year": 2077,
  "rating": 9.9,
  "description": "Low-Life and High Tech City"
}
rest = requests.post("https://28cca98109e4.ngrok-free.app/movies", json=Cyberpunk)
print(rest.json())