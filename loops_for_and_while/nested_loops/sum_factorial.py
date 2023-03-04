num, comp, sum = int(input()), 1, 0
for i_1 in range(1, num + 1):
    comp = 1
    for i_2 in range(1, i_1 + 1):
        comp *= i_2
#        print('i_1 = ', i_1, '/i_2 = ', i_2, '/sum = ', sum, '/comp = ', comp)
    sum += comp
#    print(sum)
print(sum)