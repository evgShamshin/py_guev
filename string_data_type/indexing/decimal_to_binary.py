s, total = int(input()), ''
while s:
    total += str(s % 2)
    s //= 2
#print(total)
for i in range(1, len(total) + 1):
    print(total[-i], end = '')