num, num_1, num_2= int(input()), 0, 1
print('methods_list_1', end = ' ')
if num > 1:
    for _ in range(num - 1):
        num_1, num_2 = num_2, num_1 + num_2
        print(num_2, end = ' ')
