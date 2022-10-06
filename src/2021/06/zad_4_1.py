f = open('/Users/rbaryla/Projekty/Matura/matura-python/src/2021/06/identyfikator.txt', 'r')
wyn = []
maxSum = 0
for line in f:
    mySum = 0
    for num in line[3:-1]:
        mySum += int(num)
    
    if (mySum > maxSum):
        maxSum = mySum
        wyn.clear()

    if mySum == maxSum:
        wyn.append(line)
print(wyn)

w = open('/Users/rbaryla/Projekty/Matura/matura-python/src/2021/06/wynik41.txt', 'w')
w.writelines(wyn)
w.close()

    
