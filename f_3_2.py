import random
t = []
for x in range(20):
    # n = random.randint(50, 150)
    # t.append(n)
    t.append(random.randint(50, 150))
print(t)

for e in t:
    print(e, end=' ')

# [sorozatszámítás (összegzés) tétele]
s = 0
for e in t:
    s += e

print(f'\nelemek összege: {s}')
print(f'elemek átlaga: {s / len(t)}')

avg = sum(t) / len(t)
print(f'elemek átlaga máshogy:{avg}')

# [megszámlálás tétele]
c = 0
for e in t:
    if e % 10 == 0:
        c += 1
print(f'nullára végződő elemek száma: {c}')

t.sort()

print(t)