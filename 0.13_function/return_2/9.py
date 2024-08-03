# Функция, возвращающая строку стилем написания Питона
def convert_to_snake_case(txt):
    _list = [i for i in txt if i.upper() == i and i not in '0123456789']
    for i in range(len(_list)):
        txt = txt.replace(_list[i], '_' + _list[i].lower())
    return txt[1:]

print(convert_to_snake_case(input()))