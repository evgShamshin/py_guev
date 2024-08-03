## summ - сумма цифр
## count - количество цифр
## multiply - произведение цифр
## average - среднее арифметическое цифр
## num_1 - первая цифра
## num_2 - последняя цифра
## summ_num - сумма первой и последней цифры

num, sum, count, multiply = int(input()), 0, 0, 1
num_2 = num % 10
while num:
    last_num = num % 10
    sum += last_num
    count += 1
    multiply *= last_num
    average = sum / count
    num //= 10
num_1 = last_num
summ_num = num_2 + num_1
print(sum, count, multiply, average, num_1, summ_num, sep = '\n')

