import itertools

raw = open("input.txt").readlines()
x = [int(i.strip()) for i in raw]
count=0
backlog=set()
for i in itertools.cycle(x):
    count+=i
    if count in backlog:
        print(count)
        break
    backlog.add(count)
