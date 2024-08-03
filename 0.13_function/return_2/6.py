#функция, проверяющая слово на палиндром
def pal(string):
    string = string.replace(',', '')
    string = string.replace('.', '')
    string = string.replace('!', '')
    string = string.replace('?', '')
    string = string.replace('-', '')
    string = string.replace(' ', '')
    if string[::1].lower() == string[::-1].lower():
        return True
    else:
        return False

print(pal(input()))