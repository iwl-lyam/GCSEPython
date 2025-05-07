nums = []

loooop = True
while loooop:
    to_add = (input("Enter a number pretty please - "))
    if len(nums) >= 3:
        choice = input("add to end? (y/n) ")
        if choice.lower() == "y":
            nums.append(to_add)
            print(", ".join(nums))
        else:
            print(", ".join(nums))
    else:
        nums.append(to_add)
        print(", ".join(nums))

