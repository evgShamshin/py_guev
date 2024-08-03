s = input()
count = s.count('f')
if count == 2:
    print(s.rfind('f'))
elif count > 2:
    print(s.find('f',s.find('f') + 1, len(s)))
elif count == 1:
    print(-1)
elif count == 0:
    print(-2)