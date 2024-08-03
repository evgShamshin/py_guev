num = int(input())
if (num % 7 == 0 or num % 17 == 0) and 9999 >= num >= 1000:
    print("YES")
else:
    print("NO")