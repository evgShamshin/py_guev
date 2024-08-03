#введенные строки
num_1 = int(input())
_list_1 = [input() for _ in range(num_1)]

#поисковые запросы
num_2 = int(input())
_list_2 = [input() for _ in range(num_2)]

for i_1 in _list_1:
    count = 0
    for i_2 in _list_2:
        if i_2.lower() in i_1.lower():
            count +=1
            if count == num_2:
                print(i_1)