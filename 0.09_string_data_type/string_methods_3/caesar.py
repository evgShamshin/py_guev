num = int(input())
s, s_1 = input(), 0
for c in s:
    if ord(c) - num < 96:
        s_1 = (122 - (num - (ord(c) - 96)))
    else:
        s_1 = (ord(c)) - num
    print(chr(s_1), end = '')