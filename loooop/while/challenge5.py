comp_num = 50
num = int(input("Enter a number: "))
count = 1

while num != comp_num:
    if num > comp_num:
        print("Too high")
    else:
        print("Too low")
    num = int(input("Enter a number: "))
    count += 1

print(f"You completed it after {count} guesses")
