# объявление функции
def print_digit_sum(num):
    count = 0
    for i in str(num):
        count += int(i)
    print(count)

# считываем данные
num = int(input())

# вызываем функцию
print_digit_sum(num)