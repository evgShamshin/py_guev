def get_factors(div):
    return [i for i in range(1, div + 1) if div % i == 0]

num = int(input())

print(get_factors(num))
