def is_unique(string):
    """
    Checks if a string has all unique characters (case-insensitive).

    Args:
        string: the input string

    Returns:
        True if all characters are unique, False otherwise
    """
    counter_hash = {}
    string = string.lower()
    for element in string:
        counter_hash[element] = counter_hash.get(element,0) + 1
        if counter_hash[element] > 1:
            return False

    return True


if __name__ == '__main__':
    TEST1 = "Hello"
    TEST2 = "World"
    TEST3 = "Python"
    TEST4 = "Unique"

    print(f'"{TEST1}" has all unique characters: {is_unique(TEST1)}'
          )# Should be False (has repeated 'l')
    print(f'"{TEST2}" has all unique characters: {is_unique(TEST2)}')  # Should be True
    print(f'"{TEST3}" has all unique characters: {is_unique(TEST3)}')  # Should be True
    print(f'"{TEST4}" has all unique characters: {is_unique(TEST4)}')  # Should be False
