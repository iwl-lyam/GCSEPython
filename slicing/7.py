name = input("Enter name: ").lower()
if name[0] == 'a' or name[0] == 'e' or name[0] == 'i' or name[0] == 'u' or name[0] == 'o':
    print(name[1:])
else:
    print(name)