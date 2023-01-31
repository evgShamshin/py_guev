a = float(input())
b = float(input())
c = float(input())

D = b ** 2 - 4 * a * c

if D > 0:
    if a > 0:
        x_1 = (- b + D ** 0.5) / (2 * a)
        x_2 = (- b - D ** 0.5) / (2 * a)
        print(x_2, x_1, sep = '\n')
    if a < 0:
        x_1 = (- b + D ** 0.5) / (2 * a)
        x_2 = (- b - D ** 0.5) / (2 * a)
        print(x_1, x_2, sep='\n')
elif D == 0:
    x_1 = -b / (2 * a)
    print(x_1)
elif D < 0:
    print('Нет корней')

