nevek = []

for x in range(10):
    nev = input(f'{x + 1}. név: ')
    if nev == '': break
    nevek.append(nev)
nevek.sort()
print(nevek)