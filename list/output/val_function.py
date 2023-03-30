num, _list_1, _list_2 = int(input()), list(), list()
for _ in range(num):
    _list_1.append(int(input()))
for i in _list_1:
    _list_2.append(i ** 2 + 2 * i + 1)
_list_1.append('')
print(*_list_1, *_list_2, sep = '\n')