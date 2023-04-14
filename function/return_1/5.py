def merge(list_1, list_2):
    list_1.extend(list_2)
    return sorted(list_1)

_1 = [int(i) for i in input().split()]
_2 = [int(i) for i in input().split()]

print(merge(_1, _2))