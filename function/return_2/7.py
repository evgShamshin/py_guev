#Проверка корректности пароля
def is_valid_key(key):
    key = key.split(':')
    res = True
    key_1 = int(key[1])

    # Проверка - палиндром ли число
    if key[0] != key[0][::-1]:
        res = False

    # Проверка - простое ли число
    for i in range(2, key_1):
        if key_1 % i == 0:
            res = False
            break

    # Проверка - чётное ли число
    if int(key[2]) % 2 != 0:
        res = False

    # Проверка на количество символов
    if len(key) != 3:
        res = False
    return res

print(is_valid_key(input()))