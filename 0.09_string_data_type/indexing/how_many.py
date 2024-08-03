string, count_1, count_2 = input(), 0, 0
for c in string:
    if c == '+':
        count_1 += 1
    if c == '*':
        count_2 += 1
print(f'Символ + встречается {count_1} раз', f'Символ * встречается {count_2} раз', sep = '\n')