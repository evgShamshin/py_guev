_list, num = list(), int(input())
for _ in range(num):
    c = input()
    if c not in _list:
        _list.append(c)
print(*_list, sep = '\n')