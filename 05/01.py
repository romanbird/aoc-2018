a=list("dabAcCaCBAcCcaDA")
a = list(str([i.strip() for i in open("input.txt").readlines()][0]))
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
print(length)
