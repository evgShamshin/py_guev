n = int(input())
s = 0
while n:
    l_n = n % 10
    if l_n % 2 == 0:
        s += l_n
    n //= 10
print(s)