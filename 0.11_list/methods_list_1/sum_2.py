num = int(input())
num_1, num_2 = 0, 0
_list = list()
for _ in range(num):
    num_2 = num_1
    num_1 = int(input())
    num = num_1 + num_2
    _list.append(num)
del _list[0]
print(_list)