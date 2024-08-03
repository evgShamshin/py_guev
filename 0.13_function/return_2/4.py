#функция, проверяющая корректность пароля
def password_check(key):
    flag = 0
    if is_one_alpha(key) == True: #проверка на буквенные символы (1 символ мин)
        flag += 1
    if len(key) >= 8: #проверка на длину пароля (8 символов мин)
        flag += 1
    if is_one_num(key) == True: #проверка на цифровые символы (1 символ мин)
        flag += 1
    if is_one_lower(key) == True: #проверка на нижний регистр (1 символ мин)
        flag += 1
    if is_one_upper(key) == True: #проверка на верхний регистр (1 символ мин)
        flag += 1
    if flag == 5: #проверка на количество, пройденных проверок
        return True
    else:
        return False

#функция, проверяющая есть ли в строке хотя бы одно число
def is_one_num(string):
    if len([int(i) for i in string if i in '0123456789']) >= 1:
        return True

#функция, проверяющая есть ли в строке хотя бы одна буква
def is_one_alpha(string):
    if len([i for i in string if i.upper() in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']) >= 1:
        return True

#функция, проверяющая есть ли в строке хотя бы один символ с нижнем регистре
def is_one_lower(string):
    if len([i for i in string if i == i.lower() and i.isalpha()]) >= 1:
        return True

#функция, проверяющая есть ли в строке хотя бы один символ с верхнем регистре
def is_one_upper(string):
    if len([i for i in string if i == i.upper() and i.isalpha()]) >= 1:
        return True

print(password_check(input()))