num_1, num_2, count = int(input()), int(input()), 0
for i_1 in range(num_1, num_2 + 1):
    for i_2 in range(1, i_1 + 1):
        if i_1 % i_2 == 0:
            count += 1
    if count == 2:
        print(i_1)
    count = 0