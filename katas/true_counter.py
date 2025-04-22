def count_true_values(array):
    counter = 0
    for state in array:
        if state:
            counter +=1

    return counter


if __name__ == '__main__':

    sample_array = [True, False, True, True, False]
    true_count = count_true_values(sample_array)
    print(true_count)  # 3 should be printed
