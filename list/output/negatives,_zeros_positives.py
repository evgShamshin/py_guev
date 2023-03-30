num, _list, _res = int(input()), list(), list()
for _ in range(num):
    _list.append(int(input()))
for i in _list:
    if i < 0:
        _res.append(i)
for i in _list:
    if i == 0:
        _res.append(i)
for i in _list:
    if i > 0:
        _res.append(i)
print(*_res, sep = '\n')