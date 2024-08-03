num, count, res = int(input()), 0, 0
while num:
    last_num = num % 10
    count += last_num
    num //= 10
#print(count)
while count:
    last_count = count % 10
    res += last_count
    count //= 10
if res < 10:
    print(res)
else:
    res_1 = 0
    while res:
        last_res = res % 10
        res_1 += last_res
        res //= 10
    print(res_1)