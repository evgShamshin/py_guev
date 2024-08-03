num, total = int(input()), 0
for i in range(1, num + 1):
    if i % 2 == 0:
        total -= i
    else:
        total += i
print(total)