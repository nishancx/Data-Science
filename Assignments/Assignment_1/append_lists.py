from typing import List

list_a = [1,2,3,4,5,6]
list_b = [10,20,30,40,50,60]

def append_lists(first_list:List, second_list:List)->List:
    [first_list.append(second_list[i+1]) for i in range(0,len(list_b),2)]
    return first_list

list_a = append_lists(list_a,list_b)
print(list_a)