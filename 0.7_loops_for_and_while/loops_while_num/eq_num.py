num, count = int(input()), 0
if num > 10:
    num_1 = num % 10  ## Последняя цифра числа
    num_2 = num  ## Записываем первоначальное число в переменную
    while num:
        num //= 10
        count += 1  ## Получаем количество цифр числа
    num_3 = str(num_1) * count  #Конактинируем последнее число на количество цифр
    if int(num_3) == num_2:  ##Сравниваем первоночальное число с получившимся
        print("YES")
    else:
        print("NO")
else:
    print("YES")

