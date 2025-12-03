def menu():
    return int(input("0 to exit, 1 for timetables, 2 for adding, 3 for multiplcation, 4 for subtraction, 5 for division, 6 for MOD, 7 for DIV: "))

def times_tables(product):
    for i in range(12):
        print((i+1)*product)

def add(a1,a2):
    print(a1+a2)

def mul(p1,p2):
    print(p1*p2)

def sub(a1,a2):
    print(a1-a2)

def division(d1,d2):
    print(d1/d2)

def mod(m1,m2):
    print(m1%m2)

def div(d1,d2):
    print(d1//d2)

inp = menu()
if inp == 0:
    print("bye")
elif inp == 1:
    times_tables(int(input("Enter a product: ")))
elif inp == 2:
    add(int(input("Enter a number: ")),int(input("Enter a number: ")))
elif inp == 3:
    mul(int(input("Enter a number: ")), int(input("Enter a number: ")))
elif inp == 4:
    sub(int(input("Enter a number: ")),int(input("Enter a number: ")))
elif inp == 5:
    division(int(input("Enter a number: ")),int(input("Enter a number: ")))
elif inp == 6:
    mod(int(input("Enter a number: ")),int(input("Enter a number: ")))
elif inp == 7:
    div(int(input("Enter a number: ")),int(input("Enter a number: ")))
