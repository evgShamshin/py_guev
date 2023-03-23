num = int(input())
_list = list()
for i in range(1, num + 1):
    if num % i == 0:
        _list.append(i)
print(_list)