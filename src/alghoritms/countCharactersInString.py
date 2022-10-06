S = 'Some String'
d = {}

for i in S:
    d[i] = d.get(i, 0) + 1

print(d)