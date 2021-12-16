napok = []
for x in range(12):
    asz = int(input(f'{x + 1}. napon ennyi átutalás volt: '))
    napok.append(asz)

avg = sum(napok) / len(napok)

c = 0
for n in napok:
    if n > avg: c += 1

print(f'az időszakban a napi átutalások átlaga: {round(avg, 2)}')
print(f'az átlagot {c} napon haladta meg az átutalások száma')