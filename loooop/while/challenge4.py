looping = True
count = 0
while looping:
    name = input("Who do you want to invite? ")
    print(f"{name} has been invited")
    count += 1
    cont = input("Do you want to continue?").lower()
    if cont == "n":
        looping = False

print(f"{count} people have been invited")