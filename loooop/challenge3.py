looping = True
count = 0
while looping:
    name = int(input("Number to add? "))
    print(f"{name} has been added")
    count += name
    cont = input("Do you want to continue?").lower()
    if cont == "n":
        looping = False

print(f"{count} is the sum")