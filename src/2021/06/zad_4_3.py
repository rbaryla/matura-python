f = open('/Users/rbaryla/Projekty/Matura/matura-python/src/2021/06/identyfikator.txt', 'r')
wyn = []

wagi = [7,3,1,0,7,3,1,7,3]

def myOrd(l):
    return ord(l) - 55

for line in f:
    mySum = 0
    lKon = 0
    for i in range(9):
        
        if i < 3:
            mySum += myOrd(line[i]) * wagi[i]
        elif i == 3:
            lKon = int(line[i])
        else:
            mySum += int(line[i]) * wagi[i]
    if mySum%10 != lKon:
        wyn.append(line)


w = open('/Users/rbaryla/Projekty/Matura/matura-python/src/2021/06/wynik4_3.txt', 'w')
w.writelines(wyn)
w.close()
