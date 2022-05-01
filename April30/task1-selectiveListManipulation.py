list = [1, 2, 3, 4, 5, 6, 7, 8]
newList = [x**2 for x in list if x % 3 == 0]
print(newList)