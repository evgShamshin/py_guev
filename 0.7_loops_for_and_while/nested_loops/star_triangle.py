num = int(input())
num_1 = int(num / 2 + 0.5)
for i in range(num_1 + 1):
    for _ in range(i):
        print('*', end = '')
    print()
for j in range (num_1 - 1, 0, -1):
    for _ in range(j):
        print('*', end = '')
    print()