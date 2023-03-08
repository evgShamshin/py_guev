num = int(input())
while num:
    if num < 1000:
        last_num = num % 10
        break
    else:
        last_num = num % 10
    num //= 10
print(last_num)