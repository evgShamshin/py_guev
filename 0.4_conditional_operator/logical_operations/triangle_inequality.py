A = int(input())
B = int(input())
C = int(input())

if A + C > B and A + B > C and C + B > A:
    print("YES")
else:
    print("NO")