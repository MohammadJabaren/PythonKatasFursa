def count_true_values(array):
    Counter = 0
    for bool in array:
        if bool:
            Counter +=1

    return Counter


if __name__ == '__main__':

    sample_array = [True, False, True, True, False]
    true_count = count_true_values(sample_array)
    print(true_count)  # 3 should be printed
