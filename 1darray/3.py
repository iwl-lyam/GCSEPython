names = []

for i in range(3):
    names.append(input("enter a name or else "))

stop = False
while not stop:
    if input("another? (y/n): ") == "y":
        names.append(input("enter another name then "))
    else:
        stop = True

print(len(names))