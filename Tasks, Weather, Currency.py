import requests

while True:

    print("===Tasks, Weather, Currency===")
    print("1) Get Task")
    print("2) Create Task")
    print("3) Delete Task")
    print("4) Get Weather")
    print("5) Get Available Currencies")
    print("6) Get Rate 1 To 1")
    print("7) Exit")

    apple = input("Choose Your Option : ")

    if apple == "4":
        city = input("Choose Your City : ")
        res = requests.get("https://65fdb6f97259.ngrok-free.app/weather", params={"city": city})
        weather = res.json()
        print(weather)