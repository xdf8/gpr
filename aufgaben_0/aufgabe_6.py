def max_index(lst: list):
    max_index = 0
    max_value = lst[0]
    for index, value in enumerate(lst):
        if value > max_value:
            max_index = index
            max_value = value

    return max_index


test_list = [1, 2, 3, 4, 9, 8, 7, 6, 5]

print(f'max index: {max_index(test_list)}')
print(f'max value: {test_list[max_index(test_list)]}')