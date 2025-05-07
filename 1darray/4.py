programmes = ["the lyam show", "cooking with lyam", "python for dummies with lyam", "tangent"]
for i in programmes:    print(i)

programmes.insert(int(input("Where to insert? ")), input("What's the program? "))

for i in programmes:    print(i)