num = int(input())
count_3 = 0
count_const = 0
count_2 = 0
summ_5 = 0
total_7 = 1
count_0_5 = 0
last_num_const = num % 10
while num:
    last_num = num % 10
    if last_num == 3:
        count_3 += 1
    if last_num == last_num_const:
        count_const += 1
    if last_num % 2 == 0:
        count_2 += 1
    if last_num > 5:
        summ_5 += last_num
    if last_num > 7:
        total_7 *= last_num
    if last_num == 5 or last_num == 0:
        count_0_5 += 1
    num //= 10
print(count_3, count_const, count_2, summ_5, sep = '\n')
if total_7 == 1:
    print(1)
else:
    print(total_7)
print(count_0_5)