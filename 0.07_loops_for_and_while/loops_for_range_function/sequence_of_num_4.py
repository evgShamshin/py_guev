m, n = int(input()), int(input())

if m > n:
    for j in range(m, n - 1, -1):
        print(j)

elif n >= m:
    for j in range(m, n + 1):
        print(j)