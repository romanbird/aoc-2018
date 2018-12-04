#you must forgive me
import datetime as dt
from collections import Counter
raw = open("input.txt").readlines()



class Instruction:
    def __init__(self, line):
        self.line = line
        self.year = 1518
        self.month = int(line[6:8])
        self.day = int(line[9:11])
        self.hour = int(line[12:14])
        self.minute = int(line[15:17])
        self.date = dt.datetime(self.year,self.month,self.day,self.hour,self.minute)
        self.declarative = False
        self.asleep=None
        self.id = None
        if line[19]=='G':
            self.declarative = True
            self.id = int(line[26:line.index("b")-1])
        if line[19]=='f':
            self.asleep = True

guards = dict()

x = [Instruction(i.strip()) for i in raw]
x = sorted(x, key=lambda i: i.date)

for i in x:
    if i.declarative:
        if i.id not in guards:
            guards[i.id]=[]
        current = i.id
    elif i.asleep:
        lowest = i.minute
    else:
        day = [0 for i in range(60)]
        for j in range(lowest,i.minute):
            day[j]+=1
        guards[current].append(day)



#sums = [sum(col) for col in zip(*daylog)]

#biggest_minute = (sums.index(max(sums)))
highestQuantity=0
highestGuard=None
highestIndex=None
highestV=None
for k,v in guards.items():
    if list(map(sum,zip(*v))) == []:
        continue
    if max(list(map(sum,zip(*v)))) > highestQuantity:
        highestGuard=k
        highestV=v
        highestQuantity=max(map(sum,zip(*v)))
        highestIndex=list(map(sum,zip(*v))).index(max(map(sum,zip(*v))))

indexFINAL = (list(map(sum,zip(*highestV))).index(max(map(sum,zip(*highestV)))))
print(indexFINAL)
print(highestGuard)#not 50679 or 67572
print(indexFINAL*highestGuard)





#
