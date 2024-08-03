from math import tan, pi, radians

n = int(input())
a = float(input())

S = (n * a ** 2) / (4 * tan (pi / n))

print(S)