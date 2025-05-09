def sum_of_digits(input_str):
    """
    Calculates the sum of all digits in the given string.

    Args:
        input_str: the string containing digits and other characters

    Returns:
        the sum of all digits in the string
    """

    sum = 0

    for c in input_str:
        if '1' <= c <= '9':
            sum += int(c)

    return sum


if __name__ == '__main__':
    INPUT1 = "abc1230"
    INPUT2 = "5 cats and 2 dogs"
    INPUT3 = "No digits here!"

    print(f"Sum of digits in '{INPUT1}': {sum_of_digits(INPUT1)}")  # Should be 6
    print(f"Sum of digits in '{INPUT2}': {sum_of_digits(INPUT2)}")  # Should be 7
    print(f"Sum of digits in '{INPUT3}': {sum_of_digits(INPUT3)}")  # Should be 0
