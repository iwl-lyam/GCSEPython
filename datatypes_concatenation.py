'''
datatypes_concatenation.py

Data types
'''

# CRIBS

character = 'Y'
real_float = 0.1
real_float2 = 0.2
integer = 1
string = "Hello world"
boolean = True

print(f"Floats are fun: 0.1 + 0.2 = {(real_float + real_float2):.20f}") # floating point skill issue

# It is possible to do maths with floats and integers
# It is NOT possible to do maths with strings or characters

num1 = 20.2 # floats
num2 = 30.1
total = num1 + num2
print(total)


num1 = 20 # int
num2 = 30
total = num1 + num2
print(total)

num1 = "20.2" # str
num2 = "30.1"
total = num1 + num2
print(total)

# You cannot add strings or characters
# Instead, the add symbol glues them together
# But we don't call it glue, we call it CONCATENATION

