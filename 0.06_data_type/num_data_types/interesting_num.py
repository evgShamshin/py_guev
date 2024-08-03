num = int(input())

num_1 = num // 100
num_2 = num % 100 // 10
num_3 = num % 10
num_4 = (num_1 + num_2 + num_3) - (min(num_1, num_2, num_3) + max(num_1, num_2, num_3))

if (max(num_1, num_2, num_3) - min(num_1, num_2, num_3)) == num_4:
    print("Число интересное")
else:
    print("Число неинтересное")