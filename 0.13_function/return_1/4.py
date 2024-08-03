def numbers_of_factors(div):
    return len([i for i in range(1, div + 1) if div % i == 0])

num = int(input())

print(numbers_of_factors(num))