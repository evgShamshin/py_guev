num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

if num_1 > num_2 > num_3 or num_3 > num_2 > num_1:
    print(num_2)
if num_2 > num_1 > num_3 or num_3 > num_1 > num_2:
    print(num_1)
if num_1 > num_3 > num_2 or num_2 > num_3 > num_1:
    print(num_3)