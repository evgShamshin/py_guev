_list = input().split(' ')
_list1 = []
for i in _list:
    _list1.append(int(i))
'''
print(list[_max_num])
_list[_min_num] =_list[_max_num] # число максимальное
_list[_max_num] = _list[_min_num] # число минимальное
print(list[_max_num])
print(*_list)
'''
_min = min(_list1)
_max = max(_list1)
_min_num = _list1.index(min(_list1))
_max_num = _list1.index(max(_list1))
print(_min, _max)
_list1[_max_num] = _min # число максимальное
_list1[_min_num] = _max # число минимальное
print(*_list1)