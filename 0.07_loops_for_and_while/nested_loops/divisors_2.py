num, count = int(input()), 0
for i in range(1, num + 1):
    print(i, end = '')
    for i_2 in range(1, i + 1):
        if i % i_2 == 0:
            print('+', end = '')
    print()
#    for i_2 in range(methods_list_1):
#        print('i_2 = ',у i_2, end =', ')
#    print()