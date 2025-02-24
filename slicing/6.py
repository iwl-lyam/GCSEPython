fname = input("First name: ")
lname = ""
output = ""
if len(fname) < 5:
    lname = input("Last name: ")
    name = fname + lname
    output = fname.upper()
else:
    output = fname.lower()
print(output)