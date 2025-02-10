calc = input("type y if you want to do calculator ")
if calc == "y":
    num = int(input("Num 1: "))
    num2 = int(input("Num 2: "))
    op = input("M, D, A, S").lower()
    if op == "m":
        print(num*num2)
    elif op == "d":
        print(num/num2)
    elif op == "a":
        print(num+num2)
    elif op == "s":
        print(num-num2)
    else:
        print("uh oh")
else:
    times = int(input("which time table do you want to display? "))
    for i in range(1, 13):
        print(i*times)