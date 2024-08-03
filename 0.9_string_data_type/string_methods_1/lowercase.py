s, count = input(), 0
for c in s:
    if c == c.lower() and c not in '1234567890':
        count += 1
print(count)