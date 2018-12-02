from collections import Counter
a=0
b=0
x = [Counter(i.strip()) for i in open("input.txt").readlines()]
for i in x:
    aDone=False
    bDone=False
    for v in i.values():
        if v == 2 and not aDone:
            aDone=True
            a+=1
        if v == 3 and not bDone:
            bDone=True
            b+=1
print(a*b)
