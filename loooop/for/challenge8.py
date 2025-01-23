num = int(input("How many people doth thou want to inviteth? "))

if num > 10:
    print("Nay! Thou must not overcrowd the building, we have fire safety inspectors coming tomorrow!")
else:
    for i in range(num):
        name = input("Who do you want to invite? ")
        print(f"{name} has been invited")