num = int(input())
_list = list()
s = ''
for _ in range(num):
    _list.append(input())
num = int(input())
for i in range(len(_list)):
    s = _list[i]
    if num <= len(s):
        print(s[num - 1], end = '')