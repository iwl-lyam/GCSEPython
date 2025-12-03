def menu():
    print("1) think big\n2) think bigger\n3) winning\n4) winner\n5) Exit")
    return int(input("1,2,3,4,5? "))


def inploop():
    inp = menu()
    if inp > 5:
        print("invalid choice")
        inploop()
    else:
        methods[inp-1]()

def think_big():
    print("think big selected")

def think_bigger():
    print("think bigger selected")

def winning():
    print("winning selected")

def winner():
    print("winner selected")

def exit():
    print("exit selected")

methods = [think_big, think_bigger, winning, winner, exit]
    
inploop()