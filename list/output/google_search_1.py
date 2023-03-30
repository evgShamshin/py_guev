num, _list = int(input()), list()
for _ in range(num):
    _list.append(input())
_find = input()
for i in _list:
    if _find.lower() in i.lower():
        print(i)