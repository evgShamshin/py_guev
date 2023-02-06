num_1, largest_1, largest_2 = int(input()), 0, -1
for i in range(num_1):
    num_2 = int(input())
    if num_2 > largest_1:
        largest_2 = largest_1
        largest_1 = num_2
    elif num_2 > largest_2:
        largest_2 = num_2
print(largest_1, largest_2, sep = '\n')