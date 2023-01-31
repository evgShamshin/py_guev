city_1 = input()
city_2 = input()
city_3 = input()

length_1 = len(city_1)
length_2 = len(city_2)
length_3 = len(city_3)

if length_1 < length_2 < length_3:
    print(city_1, city_3, sep ="\n")
elif length_1 < length_3 < length_2:
    print(city_1, city_2, sep ="\n")
elif length_2 < length_1 < length_3:
    print(city_2, city_3, sep ="\n")
elif length_2 < length_3 < length_1:
    print(city_2, city_1, sep ="\n")
elif length_3 < length_1 < length_2:
    print(city_3, city_2, sep ="\n")
elif length_3 < length_2 < length_1:
    print(city_3, city_1, sep ="\n")

    