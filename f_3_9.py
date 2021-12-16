rendszamok = []
sebessegek = []

for x in range(10):
    rsz = input(f'{x + 1}. rendszám: ')
    if rsz == '': break
    v = int(input(f'{x + 1}. sebesség: '))
    rendszamok.append(rsz)
    sebessegek.append(v)

print('gyorshajtók:')
c = 0
for i in range(len(rendszamok)):
    if sebessegek[i] > 90:
        print(f'{rendszamok[i]}: {sebessegek[i]} km/h')
        c += 1

if c == 0: print('nem volt gyorshajtó')

