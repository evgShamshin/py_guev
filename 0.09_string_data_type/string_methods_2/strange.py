num, count = int(input()), 0
for i in range(num):
    s = input()
    if s.count('11') >= 3:
        count += 1
print(count)