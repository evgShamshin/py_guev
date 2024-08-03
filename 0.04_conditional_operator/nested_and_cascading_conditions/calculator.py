num_1 = int(input())
num_2 = int(input())
sign = input()

if sign == "+":
    print(num_1 + num_2)
elif sign == "-":
    print(num_1 - num_2)
elif sign == "*":
    print(num_1 * num_2)
elif sign == "/":
    if num_1 != 0 and num_2 != 0:
        print(num_1 / num_2)
    elif num_2 == 0:
        print("На ноль делить нельзя!")
    elif num_1 == 0:
        print("0.0")
else:
    print("Неверная операция")