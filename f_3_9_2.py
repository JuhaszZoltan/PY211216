rendszamok = []
sebessegek = []

gyorshajtok_szama = 0
for x in range(10):
    rsz = input(f'{x + 1}. rendszám: ')
    if rsz == '': break
    v = int(input(f'{x + 1}. sebesség: '))
    if v > 90: gyorshajtok_szama += 1
    rendszamok.append(rsz)
    sebessegek.append(v)

if gyorshajtok_szama > 0:
    for i in range(len(rendszamok)):
        if sebessegek[i] > 90:
            print(f'{rendszamok[i]}: {sebessegek[i]} km/h')
else: print('nem volt gyorshajtó')