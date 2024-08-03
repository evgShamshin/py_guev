colour_1 = input()
colour_2 = input()

colour = colour_1 + colour_2

if (colour_1 == "красный" and colour_2 == "синий") or (colour_2 == "красный" and colour_1 == "синий"):
    print("фиолетовый")

elif (colour_1 == "синий" and colour_2 == "желтый") or (colour_2 == "синий" and colour_1 == "желтый"):
    print("зеленый")

elif (colour_1 == "красный" and colour_2 == "желтый") or (colour_2 == "красный" and colour_1 == "желтый"):
    print("оранжевый")

else:
    print("ошибка цвета")