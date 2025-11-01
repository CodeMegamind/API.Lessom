import requests


while True:

    print("===Movies===")
    print("1) List movies")
    print("2) Get one")
    print("3) Create")
    print("4) Update (partial)")
    print("5) Delete")
    print("0) Exit")


    Diddy = input("Choose Your Option :")

    if Diddy == "1":
       print("list of movies")
       res = requests.get("https://9958d672d07b.ngrok-free.app/movies")
       movies = res.json()
       for movie in movies:
           print("ID:",movie["id"])
           print("Title", movie["title"])
           print("Year", movie["year"])
           print("Rating", movie["rating"])
           print("Description", movie["description"])
           print("------------")
    if Diddy == "3":
        print("Create")
        Dave = input("Title")
        Bob = int(input("Year"))
        Jack = int(input("Rating"))
        Van = input("Description")
        res = requests.post("https://9958d672d07b.ngrok-free.app/movies", json=
            {

                "title": Dave,
                "year": Bob,
                "rating": Jack,
                "description": Van

            })
        print(res.json())

    if Diddy == "5":
        print("Delete")
        id = input("input id: ")
        res = requests.delete(f"https://9958d672d07b.ngrok-free.app/movies/{id}")
