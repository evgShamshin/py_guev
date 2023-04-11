number = input().split('-')
_total = []
s = 'YES'
for i in number:
    if s != 'NO':
        _total.append(len(i))
        for i_1 in i:
            if i_1 not in '01234567890':
                s = 'NO'
                print(s)
                break

if s != 'NO':
    if (_total == [1,  3,  3, 4] and number[0] == '7') or (_total == [3, 3, 4]):
        print(s)
    else:
        s = 'NO'
        print(s)