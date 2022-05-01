"""Program to convert list to dict conditionally"""

keys_list = [1, 2, 3, 4]
values_list = ['a', 'b', 'c', 'd']
my_dict = {5: 'e', 6: 'f'}

def convert_list_to_dict(dict_a:dict, list_keys:list, list_values:list):
    """Convert list to dict conditionally

    Args:
        dict_a (_type_): _description_
        list_keys (_type_): _description_
        list_values (_type_): _description_
    """

    for key in list_keys:
        if key not in dict_a:
            dict_a[key] = list_values[key - 1]
    print(dict_a)

convert_list_to_dict(my_dict, keys_list, values_list)
