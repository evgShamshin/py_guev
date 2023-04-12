# объявление функции
def print_fio(name, surname, patronymic):
    print(surname.upper()[0], name.upper()[0], patronymic.upper()[0], sep='')

# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)