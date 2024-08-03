s, c_t, count_t = input(), '', 0
for c in s:
    count_0 = 0
    for i in range(len(s)):
        count_0 = s.count(str(c))
        if count_0 >= count_t:
            count_t = count_0
            c_t = c
print(c_t)