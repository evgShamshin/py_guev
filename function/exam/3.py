def compute_binom(n, k):
    from math import factorial
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

print(compute_binom(int(input()), int(input())))