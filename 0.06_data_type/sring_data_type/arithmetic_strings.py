num_1 = input()
num_2 = input()
num_3 = input()

length_1 = len(num_1)
length_2 = len(num_2)
length_3 = len(num_3)

if length_1 - length_2 == length_3 - length_1:
    print("YES")
elif length_1 - length_3 == length_2 - length_1:
    print("YES")
elif length_2 - length_1 == length_3 - length_2:
    print("YES")
elif length_2 - length_3 == length_1 - length_2:
    print("YES")
elif length_3 - length_2 == length_1 - length_3:
    print("YES")
elif length_3 - length_1 == length_2 - length_3:
    print("YES")
else:
     print("NO")

