s, count = input(), 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
    print(s[i], s[i + 1])
print(count)