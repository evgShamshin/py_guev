def get_month(lng, num):
    lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь',
              'октябрь', 'ноябрь', 'декабрь']

    lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september',
              'october', 'november', 'december']
    if lng == 'ru':
        return lng_ru[num - 1]

    if lng == 'en':
        return lng_en[num - 1]


print(get_month(input(), int(input())))