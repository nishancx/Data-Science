"""_summary_"""
list_a = [1, 2, 3, 4, 5, 6]
list_b = [10, 20, 30, 40, 50, 60]

list_a.extend(list_b[1::2])
print(list_a)
