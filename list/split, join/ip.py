flag = ''
for i in input().split('.'):
    if 0 <= int(i) <= 255:
        flag = 'ДА'
    else:
        flag = 'НЕТ'
        break
print(flag)