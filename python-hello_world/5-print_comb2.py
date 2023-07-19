for num in range (0, 100):
    if num < 10:
        print("0{},".format(num), end=" ")
    elif num == 99:
        print(num)
    else:
        print("{},".format(num), end=" ")
