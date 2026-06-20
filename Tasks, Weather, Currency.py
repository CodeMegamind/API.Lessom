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
        res = requests.get("https://apilesson2.vercel.app/weather", params={"city": city})
        weather = res.json()
        print("City", weather["city"])
        print("Latitude", weather["latitude"])
        print("Longitude", weather["longitude"])
        print("Temperature", weather["temperature_c"])
        print("Wind_Speed", weather["wind_speed"])

    if apple == "1":
        res = requests.get("https://apilesson2.vercel.app/tasks")
        tasks = res.json()
        print("Tasks")
        print(tasks)

    if apple == "2":
        task = input("Create Your Task : ")
        orange={
            "title": task
        }
        res = requests.post("https://apilesson2.vercel.app/tasks", json=orange)
        print(res.text)



