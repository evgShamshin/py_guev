num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

num_4 = (num_1 + num_2 + num_3) - (min(num_1, num_2, num_3) + max(num_1, num_2, num_3))
print(max(num_1, num_2, num_3))
print(num_4)
print(min(num_1, num_2, num_3))