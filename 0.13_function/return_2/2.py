def is_prime(num):
    if len([i for i in range(2, num) if i >= 1 and num % i != 0]) == num - 2:
        return True
    else:
        return False

n = int(input())
print(is_prime(n))