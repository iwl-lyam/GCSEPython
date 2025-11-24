with open("names.txt", "r+") as names:
    print(names.read())
    names.write(names.read()+"\n"+input("Enter a name: "))