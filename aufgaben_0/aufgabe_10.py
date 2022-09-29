def kaprekar_4(number):
    number = str(number)
    prev_num = 0
    if len(number) < 4:
        number = number.rjust(4, '0')
    while int(number) != int(prev_num):
        prev_num = str(number)
        number = str(number)
        min_num = ''
        max_num = ''
        min_num_list = sorted(number, reverse = False)
        max_num_list = sorted(number, reverse = True)
        for i in min_num_list:
            min_num = min_num + i

        for i in max_num_list:
            max_num = max_num + i

        number = int(max_num) - int(min_num)

    return number

print(kaprekar_4(number = 1337))