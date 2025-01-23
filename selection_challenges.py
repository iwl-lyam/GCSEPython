'''
#1
num1 = int(input("number 1 "))
num2 = int(input("number 2 "))

if num1 > num2:
    print(f"{num2} {num1}")
elif num2 > num1:
    print(f"{num1} {num2}")

#2
num = int(input("enter number "))
if num >= 20:
    print("too high")
else:
    print("thank you")

#3
num = int(input("enter number "))

if num >= 10 and num <= 20:
    print("thank you")
else:
    print("incorrect answer")

#4
colour = input("enter a colour ")
if colour.lower() == "red":
    print("I like red too")
else:
    print(f"I don't like {colour}, {colour} is for losers")

#5
rain = input("is it raining? ").lower()

if rain == "yes":
    wind = input("is it windy? ").lower()
    if wind == "yes":
        print("you're going to get wet")
    else:
        print("you're safe, take an umbrella")
else:
    print("no rain, no umbrella")

#6
age = int(input("enter age "))

if age >= 18:
    print("you can vote")
elif age == 17:
    print("you can learn to drive")
elif age == 16:
    print("you can buy a lottery ticket")
else:
    print("you can trick or treat")

#7
num = int(input("enter number "))

if num >= 10 and num <= 20:
    print("thank you")
elif num > 20:
    print("too high you crazy pizza pie")
elif num < 10:
    print("too low")

#8
num = input("enter 1 2 or 3")

if num == "1":
    print("thank you")
elif num == "2":
    print("well done you're so smart")
elif num == "3":
    print("amazing, you're so good at this")
else:
    print("really?? what is wrong with you??")

'''
