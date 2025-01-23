total = 0

for i in range(5):
    num = int(input("Enter a number: "))
    cont = input("Do you want to add it to the sum?").lower()
    if cont == "y":
        total += num

print(f"Sum is {total}")