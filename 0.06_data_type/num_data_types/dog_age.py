n = int(input())

if n <= 2:
    age = n * 10.5
else:
    age = (2 * 10.5) + (4 * (n-2))

print (age)