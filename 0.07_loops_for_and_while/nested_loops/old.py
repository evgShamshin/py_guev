# cow = 5 bull = 10 calf = 0.5
total = 0
for cow in range(1, 100):
    for bull in range(1, 100):
        for calf in range(1, 100):
            if 5 * cow + 10 * bull + 0.5 * calf == 100 and cow + bull + calf == 100:
                print(f'calf = {calf}', f'bull = {bull}', f'cow = {cow}')
print(total)

