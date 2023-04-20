def is_magic(date):
    _list = [int(i) for i in date.split('.')]
    _3 = _list[2] % 100
    if _list[0] * _list[1] == _3:
        return True
    else:
        return False

print(is_magic(input()))