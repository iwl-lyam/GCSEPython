print("open file")
while True:
    with open("text.txt", "a+") as file
        file.write(input("enter stuff >> "))
        print(file.read())

