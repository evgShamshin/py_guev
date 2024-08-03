num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
num_4 = int(input())

if num_1 > num_2:
    num_1 = num_2
else:
    num_2 = num_1

if num_3 > num_4:
    num_3 = num_4
else:
    num_4 = num_3

if num_1 > num_3:
    print(num_3)
else:
    print(num_1)