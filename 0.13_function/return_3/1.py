def get_point(x_1, y_1, x_2, y_2):
    return (x_1 + x_2) / 2, (y_1 + y_2) / 2

print(*(get_point(float(input()), float(input()), float(input()), float(input()))))