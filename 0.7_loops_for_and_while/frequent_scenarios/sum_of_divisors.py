num, sum = int(input()), 0
for i in range(1, num + 1):
    if (num % i == 0) or (num % i == num):
        sum += i
        print(sum)
print(sum)