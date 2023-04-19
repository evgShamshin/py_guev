def get_next_prime(num):
    flag = False
    while flag == False:
        num += 1
        if len([i for i in range(2, num) if i >= 1 and num % i != 0]) == num - 2:
            flag = True
            return num

n = int(input())
print(get_next_prime(n))