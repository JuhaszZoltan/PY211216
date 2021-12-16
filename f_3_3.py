import random

# v1
t = []
for x in range(20):
    t.append(random.randint(10, 99))
t.sort()
print(t)

# v2
t = []
k = 10
for x in range(20):
    n = random.randint(k, 99)
    t.append(n)
    k = n
print(t)

#v3
t = []
k = 10
dif = (99 - 10) / 20
n = k + dif
for x in range(20):
    k = random.randint(k, int(n))
    t.append(k)
    n += dif
print(t)