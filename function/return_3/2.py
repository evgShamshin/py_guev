def get_circle(radius):
    from math import pi
    C = 2 * pi * radius # Длина окружности
    S = pi * radius**2 # Площадь окружности
    return C, S

print(*(get_circle(float(input()))))