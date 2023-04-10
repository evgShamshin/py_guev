num = input()[1:]
_list = [input() for _ in range(int(num))]

for i in _list:
    if '#' in i:
        print(i[:i.index('#')].rstrip())
    else:
        print(i)