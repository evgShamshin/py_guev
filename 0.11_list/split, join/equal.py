_list, count = list(), 0
for i in input().split():
    _list.append(int(i))
for i in range(len(_list)):
    for i2 in range(i + 1, len(_list)):
        if _list[i] == _list[i2]:
            count += 1
print(count)