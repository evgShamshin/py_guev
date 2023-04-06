_list = input().lower().split()
print('Общее количество артиклей:', end = ' ')
print(_list.count('a') + _list.count('an') + _list.count('the'))