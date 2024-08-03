def is_one_away(_1, _2):
    count = 0
    for i in range(len(_1)):
        if _1[i] == _2[i]:
            count += 1
    if count == len(_1) - 1:
        return True
    else:
        return False

print(is_one_away(input(), input()))