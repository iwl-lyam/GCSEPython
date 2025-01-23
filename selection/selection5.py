rain = input("is it raining? ").lower()

if rain == "yes":
    wind = input("is it windy? ").lower()
    if wind == "yes":
        print("you're going to get wet")
    else:
        print("you're safe, take an umbrella")
else:
    print("no rain, no umbrella")