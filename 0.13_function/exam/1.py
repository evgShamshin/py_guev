def get_triangle(a, h):
    for i in range(1, h * 2 + 1, 2):
        space = ' ' * ((a - i) // 2)
        print(space + '*' * i)

get_triangle(15, 8)