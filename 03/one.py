import numpy as np #external dependency
class claim:
    def __init__(self, line):
        self.id = line[:line.index(" ")]
        self.xd = int(line[line.index("@")+2:line.index(",")])
        self.yd = int(line[line.index(",")+1:line.index(":")])
        self.x = int(line[line.index(":")+2:line.index("x")])
        self.y = int(line[line.index("x")+1:])

raw = open("input.txt").readlines()
claims = [claim(i) for i in raw]

matrix = np.zeros(shape=(1000,1000))

for claim in claims:
    for row in range(claim.xd, claim.xd+claim.x):
        for column in range(claim.yd, claim.yd+claim.y):
            matrix[row,column]+=1
    

count = 0
print(matrix)
for i in matrix:
    for x in i:
        if x > 1:
            count+=1
print(count)
