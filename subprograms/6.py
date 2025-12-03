def menu():
    return int(input("0 to exit, 1 for timetables: "))

def times_tables(product):
    for i in range(12):
        print((i+1)*product)

inp = menu()
if inp == 0:
    print("bye")
elif inp == 1:
    times_tables(int(input("Enter a product: ")))

