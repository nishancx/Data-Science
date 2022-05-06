from typing import List, Dict

name = ['Gita', 'Ram', 'Shyam', 'Sita', 'Gita']
percentage = [70, 40, 60, 90, 70]
marks_dict = {}

for index, student  in enumerate(name):
  if percentage[index] > 50:
    marks_dict[student] = percentage[index]

print(marks_dict)