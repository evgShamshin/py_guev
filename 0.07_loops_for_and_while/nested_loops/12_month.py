#28n + 30k + 31m = 365
total = 0
for n in range(1, 13):
    for k in range(1, 12):
        for m in range(1, 11):
            if 28 * n + 30 * k + 31 * m == 365:
                print(f'n={n}', f'k = {k}', f'm = {m}')
                total += 1
print(total)