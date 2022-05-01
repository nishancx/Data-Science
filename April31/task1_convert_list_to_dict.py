"""Program to convert list to dict conditionally"""

def convert_list_to_dict(myDict:dict, keysList:list, listValues:list):
    """Convert list to dict conditionally

    Args:
        dict_a (_type_): _description_
        list_keys (_type_): _description_
        list_values (_type_): _description_
    """

    for key in keysList:
        if key not in myDict:
            myDict[key] = listValues[key - 1]
    print(myDict)

convert_list_to_dict({5: 'e', 6: 'f'}, [1, 2, 3, 4], ['a', 'b', 'c', 'd'])
