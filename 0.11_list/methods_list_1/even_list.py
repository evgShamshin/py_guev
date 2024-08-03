num = int(input())
_list = list()
for i in range(num):
    _list.append(int(input()))
del _list[1::2]
print(_list)
