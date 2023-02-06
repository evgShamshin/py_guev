total = ""
for _ in range(10):
    num = int(input())
    if num % 2 != 0:
        total += "н"
    else:
        total += "ч"
if "н" in total:
    print("NO")
else:
    print("YES")