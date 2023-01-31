a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a-c)**2==(b-d)**2:
    print("YES")

else:
    if (a == c) or (b == d):
        print("YES")

    else:
        print("NO")

