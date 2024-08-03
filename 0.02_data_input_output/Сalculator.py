num_1 = int(input())
num_2 = int(input())
sign = input("Введите арифметический знак: ")
if sign!=0:
    if sign == "+":
        print(num_1 + num_2)
    if sign== "-":
        pri nt(num_1 - num_2)
    if sign== "*":
        print(num_1 * num_2)
    if sign== "/":
        print(num_1 / num_2)
    else:
        print("404 not found")