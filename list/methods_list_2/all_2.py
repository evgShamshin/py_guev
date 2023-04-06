numbers = [8, 9, 10, 11]
numbers.remove(9)
numbers.insert(1, 17) # numbers[1] = 17 Заменил второй элемент списка на 17
for i in "456": # Добавил числа 4, 5 и 6 в конец списка
    numbers.append(int(i))
numbers.pop(0) # Удалил первый элемент списка
numbers *= 2 #Удвоил список
numbers.insert(3, 25) # Вставил число 25 по индексу 3
print(numbers) # Вывел список, с помощью функции print()