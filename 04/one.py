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
guards_count=dict()

x = [Instruction(i.strip()) for i in raw]
x = sorted(x, key=lambda i: i.date)

for i in x:
    if i.declarative:
        if i.id not in guards:
            guards[i.id]=[]
            guards_count[i.id]=0
        current = i.id
    elif i.asleep:
        lowest = i.minute
    else:
        day = [0 for i in range(60)]
        for j in range(lowest,i.minute):
            day[j]+=1
        guards[current].append(day)
        guards_count[current]+=(i.minute-lowest)

biggest_sleeper = max(guards_count, key=guards_count.get)

daylog = guards[biggest_sleeper]


sums = [sum(col) for col in zip(*daylog)]

biggest_minute = (sums.index(max(sums)))


print(biggest_minute)
print(biggest_sleeper)

print(biggest_minute*biggest_sleeper)












#
