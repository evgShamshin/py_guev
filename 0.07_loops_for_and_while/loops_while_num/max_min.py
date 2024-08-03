num, num_1, num_2 = int(input()), 0, 10
while num != 0:
    last_num = num % 10
    if num_1 < last_num:
        num_1 = last_num
    if num_2 > last_num:
        num_2 = last_num
    num //= 10
print(f'Максимальная цифра равна {num_1}', f'Минимальная цифра равна {num_2}', sep = '\n')