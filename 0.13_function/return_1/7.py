# объявление функции
def get_days(month):
    return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))