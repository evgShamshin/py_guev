_list = input().split()
for i in range(len(_list)):
    _list[i] = int(_list[i])
_list.sort()
print(*_list)
_list.sort(reverse=True)
print(*_list)