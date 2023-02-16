num = int(input())
for i in range(2, num):
    if num % i == 0:
        num = i
        break
print(num)