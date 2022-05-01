"""Program to convert list to dict conditionally"""

def convert_list_to_dict(my_dict:dict, keys_ist:list, values_list:list):
    """convert list to dict conditionally

    Args:
        my_dict (dict): dict to be added onto
        keys_ist (list): list of keys
        values_list (list): list of values
    """

    for key in keys_ist:
        if key not in my_dict and len(values_list) > key:
            my_dict[key] = values_list[key]

    print(my_dict)

convert_list_to_dict({5: 'e', 6: 'f'}, [1, 2, 3, 4], ['a', 'b', 'c', 'd'])
