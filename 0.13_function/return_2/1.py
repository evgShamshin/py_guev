def is_valid_triangle(A, B, C):
    if A + C > B and A + B > C and C + B > A:
        return True
    else:
        return False

print(is_valid_triangle(int(input()), int(input()), int(input())))