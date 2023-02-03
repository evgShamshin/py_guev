m, n = int(input()), int(input())

if m > n:
    for k in range(m, n - 1, -1):
        print(k)

elif n >= m:
    for k in range(m, n + 1):
        print(k)