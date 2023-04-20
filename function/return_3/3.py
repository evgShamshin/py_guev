def solve(a, b, c):
    D = b ** 2 - 4 * a * c
    if D > 0:
        if a > 0:
            x_1 = (- b + D ** 0.5) / (2 * a)
            x_2 = (- b - D ** 0.5) / (2 * a)
            return x_2, x_1
        if a < 0:
            x_1 = (- b + D ** 0.5) / (2 * a)
            x_2 = (- b - D ** 0.5) / (2 * a)
            return x_1, x_2
    if D == 0:
        x_1 = -b / (2 * a)
        return x_1, x_1

print(*(solve(float(input()), float(input()), float(input()))))
