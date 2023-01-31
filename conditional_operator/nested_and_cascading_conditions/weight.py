weight = int(input())

if weight < 60:
    print ("Легкий вес")
elif 60 <= weight < 64:
    print("Первый полусредний вес")
elif weight >= 64:
    print("Полусредний вес")