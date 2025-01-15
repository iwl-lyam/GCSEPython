'''
input_casting.py
Explaining inputs and casting ig
'''

# Input is a function
# It allows a user to input data into
# ...a program via the keyboard
# It can also display strings
# Here is a variable
name = ""
# Here is a variable with input
name = input("enter name ")
age = input("enter age ")
colour = input("enter favourite colour ")

# This will display "enter name"
# aaaaaa this is ssooo boring
# The user should then enter a string
# Then press enter
# The data entered will be stored in the variable
# This data can be displayed later
print(f"You are {name}, you are {age} years old, and your favourite colour is {colour}.\n\n\tThank you for using the Lyam personal information tracking service!\n\tI can assure you it will not be sold to advertisers.") # woah truly shocking

# casting introduced
# casting is a way to change data types
# example:

age_int = int(age)
total = age_int+10
print(total)

# the following functionsssssssssssssssss allow you to casttstst
# int() str() float() bool()
