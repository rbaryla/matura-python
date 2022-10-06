f = open('/Users/rbaryla/Projekty/Matura/matura-python/src/2021/06/identyfikator.txt', 'r')
wyn = []
maxSum = 0
def isPoli(w):
    print(w)
    for i in range(3):
        if w[i] != w[(i+1)*-1]:
            return False
    return True
for line in f:
    if line[0] == line[2]:
        wyn.append(line)
    else:
        if isPoli(line[3:-1]):
            wyn.append(line)

w = open('/Users/rbaryla/Projekty/Matura/matura-python/src/2021/06/wynik4_2.txt', 'w')
w.writelines(wyn)
w.close()
