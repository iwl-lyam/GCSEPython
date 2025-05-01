cars = []
wait = True

while wait:
    inp = input("input a car brand or presssss x to exit ")

    if inp == "x":
        wait = False
    else:
        cars.append(inp)

print("In the list is", cars)

