import itertools
x = [i.strip() for i in open("input.txt").readlines()]
for a,b in itertools.combinations(x, 2):
    common=str()
    for n,i in enumerate(a):
        if i == b[n]:
            common+=i
    if len(common)==len(a)-1:
        print(common)
