num_people = int(input())
if num_people>1:
    num_alive = round(num_people/2)
else:
    num_alive = round(num_people)
print(num_alive)