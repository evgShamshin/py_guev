num = int(input())
_list = list()
for _ in range(num):
    _list.append(int(input()))
for i in range(len(_list)):
    if _list[i] == min(_list):
        continue
    elif _list[i] == max(_list):
        continue
    else:
        print(_list[i])