count, maximum = 0, 0
for _ in range(8):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x
if count == 0:
    print('NO')
else:
    print(count)
    print(maximum)