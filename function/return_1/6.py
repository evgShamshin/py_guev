def find_all(target, symb):
    return [x for x in range(len(target)) if target[x] == symb]

print(find_all("ававав", "а"))