def run():
    fname = input("enter first name? ")
    lname = input("enter last name? ")
    age = input("enter age? ")
    file = open("data.txt", "a")
    file.write(f"{fname} {lname}: {age}\n")
    if input("write another user? ").lower() == "y":
        file.close()
        run()
    file.close()
run()