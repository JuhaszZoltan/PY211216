class Vezeto:
    def __init__(self, rsz, seb):
        self.rendszam = rsz
        self.sebesseg = seb

vezetok = []
for x in range(10):
    rsz = input(f'{x + 1}. rendszám: ')
    if rsz == '': break
    seb = int(input(f'{x + 1}. sebesség: '))
    vezetok.append(Vezeto(rsz, seb))

gyorshajtok = []

for v in vezetok:
    if v.sebesseg > 90:
        gyorshajtok.append(v)

if len(gyorshajtok) > 0:
    print('gyorshajtok: ')
    for gy in gyorshajtok:
        print(f'{gy.rendszam}: {gy.sebesseg} Km/h')
else: print('nem volt gyorshajtó')