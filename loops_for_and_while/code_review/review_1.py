count = 0
total = 1
for _ in range(10):
    num = int(input())
    if num >= 0:
        total *= num
        count += 1
if count != 0:
    print(count)
    print(total)
else:
    print('NO')