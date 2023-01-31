num = 333
num_1 = num//100
num_2 = (num%100)//10
num_3 = (num%100)%10
print(f"Сумма цифр = {num_1 + num_2 + num_3}", f"Произведение цифр = {num_1 * num_2 * num_3}", sep = "\n")