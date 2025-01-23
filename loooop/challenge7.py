num = 10
while num > 0:
    print(f"there are {num} green bottles on the wall, there are aaa you get the idea")
    while int(input("How many bottles are hanging on the wall? ")) != num-1:
        print("Try again!")
    print("There'll be",num-1,"bottles hanging on the wall")
    num -= 1

print("There are no more green bottles on the wall.")

