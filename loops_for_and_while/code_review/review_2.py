mx = -10 ** 7 #1 mx = 0
s = 0
for _ in range(10): #2 for i in range(11):
    x = int(input())
    if x < 0:
        s += x #3 s = x
        if x > mx: #4 if x > mx:
            mx = x
if s != 0: #5
    print(s)
    print(mx)
else: #5
    print("NO")