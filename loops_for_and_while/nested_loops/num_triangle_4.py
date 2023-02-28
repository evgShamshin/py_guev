num, count = int(input()), 0
for i in range(1, num + 1):
    for k in range(1, i):
        print(k, end = '')
    for j in range(i, 0, -1):
        print(j, end = '')
    print()