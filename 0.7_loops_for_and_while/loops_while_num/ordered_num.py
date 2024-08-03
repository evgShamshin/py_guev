num, num_1, mark = int(input()), 0, ''
while num:
    last_num = num % 10
    if last_num >= num_1:
        num_1 = last_num
        mark = 'YES'
    else:
        mark = 'NO'
        break
    num //= 10
print(mark)