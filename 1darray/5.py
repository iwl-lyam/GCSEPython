food = []
for i in range(4):  food.append(input("enter a food: "))

print(", ".join(food))

del food[int(input("which to delete? ")) - 1]

print(", ".join(food))
