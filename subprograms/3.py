def menu():
    print("1) 1-player\n2) 2-player\n3) Online\n4) Exit")
    return int(input("1,2,3,4? "))

match menu():
    case 1:
        print("1 player selected")
    case 2:
        print("2 player selected")
    case 3:
        print("online selected")
    case 4:
        print("exiting")
    
