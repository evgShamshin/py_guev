num, count = int(input()), -1
num_1 = num
while num:
    count += 1
    num //= 10
num_1 = (num_1 % (10**count)) // 10**(count-1)
print(num_1)