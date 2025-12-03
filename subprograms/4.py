def menu():
    print("1) creative\n2) survival\n3) hardcore\n4) adventure\n5) Exit")
    return int(input("1,2,3,4? "))

def inploop():
    match menu():
        case 1:
            print("creative selected")
        case 2:
            print("survival selected")
        case 3:
            print("hardcore selected")
        case 4:
            print("adventure")
        case 5:
            print("exiting")
        case _:
            print("invalid choice")
            inploop()
    
inploop()