num, total = int(input()), 0
while num >= 25:
    total += num // 25
    num %= 25
while 10 <= num < 25:
    total += num//10
    num %= 10
while 5 <= num < 10:
    total += num // 5
    num %= 5
while 1 <= num < 5:
    total += num // 1
    num %= 1
print(total)