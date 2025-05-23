

def flatten_list(nested_list):
    """
    Flattens a nested list into a single list of integers.

    Args:
        nested_list: the input nested list

    Returns:
        a flat list containing all integers from the nested structure
    """
    # hint: isinstance()
    flat = []
    flatten_list_helper(nested_list,flat)
    return flat

def flatten_list_helper(nested_list,flat):
    for element in nested_list:
        if isinstance(element,list):
            flatten_list_helper(element,flat)

        else:
            flat.append(element)

    return flat



if __name__ == '__main__':
    nested_list_2 = [
        1,
        [2, 3],
        [4, [5, 6]],
        7
    ]

    flat_list = flatten_list(nested_list_2)

    print(f"Flattened list: {flat_list}")  # Should be [1, 2, 3, 4, 5, 6, 7]
