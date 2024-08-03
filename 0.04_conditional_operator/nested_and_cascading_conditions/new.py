a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if a2 > a1:
    if b1 > a2 and b1 >= b2:
        print(a2, b2)
    if b1 > a2 and b1 < b2:
        print(a2, b1)
    elif b1 < a2:
        print("пустое множество")
    if b1 == a2:
        print(b1)

else:
    if b2 > a1 and b2 >= b1:
        print(a1, b1)
    elif b2 > a1 and b2 < b1:
        print(a1, b2)
    elif b2 < a1 :
        print("пустое множество")
    elif b2 == a1:
        print(b2)




