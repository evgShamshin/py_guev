num_1, num_2 = int(input()), int(input())  # начало/конец цикла
count_0, count_1, count_2 = 0, 0, 0  # счётчик суммы делителей
div_1, div_2 = 0, 1  # переменные для записи членов из methods_list_1 цикла
num_max, count_max = 0, 0  # число с макс. суммой дилителей

for i in range(num_1, num_2):
    div_1, div_2 = i, i + 1
    count_1, count_2 = 0, 0
    for i_1 in range(1, i + 2):
        if div_1 % i_1 == 0:
             count_1 += i_1
        if div_2 % i_1 == 0:
            count_2 += i_1
    if count_2 >= count_max:
        num_max = div_2
        count_max = count_2
    if count_1 >= count_max:
        num_max = div_1
        count_max = count_1
    print(i, num_max, count_max, count_1, count_2)

print(num_max, count_max)