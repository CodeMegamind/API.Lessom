import requests

res = requests.get("https://28cca98109e4.ngrok-free.app/movies")
movies = res.json()

print(movies[1])
print(movies[1]["title"])

for movie in movies:
    print(movie["title"])