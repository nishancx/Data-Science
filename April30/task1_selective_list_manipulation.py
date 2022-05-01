"""Square numbers divisible by 3 from a list"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
newList = [x**2 if x % 3 == 0 else x for x in my_list]
print(newList)
