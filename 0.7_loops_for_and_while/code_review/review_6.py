n, total = int(input()), 1
while n:
    last_num = n % 10
    total *= last_num
    n //= 10
print(total)