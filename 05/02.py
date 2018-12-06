#raw="dabAcCaCBAcCcaDA"
raw= (str([i.strip() for i in open("input.txt").readlines()][0]))

def collapse(a):
    a=list(a)
    running=True
    while running:
        while True:
            dirtyLoop = False
            for n in range(len(a)-1):
                if abs(ord(a[n])-ord(a[n+1]))==32:
                    dirtyLoop = True
                    del a[n]
                    del a[n]
                    break
            if dirtyLoop and len(a)>1:
                length = len(a)
                break
            else:
                running=False
                break
    return length

lengths=[]

for i in "abcdefghijklmnopqrstuvwxyz":
    lengths.append(collapse(raw.replace(i,"").replace(i.swapcase(),"")))

print(min(lengths))
