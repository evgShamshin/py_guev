num_place = int(input())
num_rest = num_place%4
print(num_rest)
if num_rest == 1 or 2:
    num_booth = round((num_place/4)+0.30)
else:
    num_booth = round(num_place/4)
print(num_booth)