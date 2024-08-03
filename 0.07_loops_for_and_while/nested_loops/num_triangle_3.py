num, count = int(input()), 0
for i in range(1, num + 1):
    for k in range(1, i + 1):
        count += 1
        print(count, end = ' ')
    print()