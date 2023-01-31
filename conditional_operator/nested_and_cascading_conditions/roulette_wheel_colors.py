num = int(input())

if num == 0:
    print("зеленый")

elif 1 <= num <= 10 or 19 <= num <= 28:
    if num % 2 != 0:
        print("красный")
    if num % 2 == 0:
        print("черный")

elif 11 <= num <= 18 or 29 <= num <= 36:
    if num % 2 != 0:
        print("черный")
    if num % 2 == 0:
        print("красный")

else:
    print("ошибка ввода")