num = int(input("Enter a number: "))
while num < 10 or num > 20:
    if num > 20:
        print("too high")
    else:
        print("too low")
    num = int(input("Enter a number: "))
print("correct")