s, total = int(input()), ''
while s:
    total = str(s % 2) + total
    s //= 2
print(total)