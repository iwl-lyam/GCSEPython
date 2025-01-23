dir = input("U or D ").lower()
num = int(input("I decree that thou giveth me a number at once: "))

if dir == "u":
    for i in range(num, 99999999999999999999999999999999999):
        print(i)
elif dir == "d":
    for i in range(num, -99999999999999999999999999999999, -1):
        print(i)
else:
    print("The emperor is really disapointed.")
