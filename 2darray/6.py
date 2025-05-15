empty_array = [[0 for _ in range(int(input("columns? ")))] for _ in range(int(input("rows? ")))]
empty_array[int(input("row? "))][int(input("column? "))] = input("data? ")
print(empty_array)

