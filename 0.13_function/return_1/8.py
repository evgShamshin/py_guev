def merge_2(num):
    _list = []
    for i in range(num):
        _list += input().split()
    _list = [int(i) for i in _list]
    return sorted(_list)

n = int(input())

print(* merge_2(n))