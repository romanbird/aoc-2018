import numpy as np #external dependency
from collections import Counter
class claim:
    def __init__(self, line):
        self.id = int(line[1:line.index(" ")])
        self.xd = int(line[line.index("@")+2:line.index(",")])
        self.yd = int(line[line.index(",")+1:line.index(":")])
        self.x = int(line[line.index(":")+2:line.index("x")])
        self.y = int(line[line.index("x")+1:]) #forgot a colon here which had to break EVERYTHING

raw = open("input.txt").readlines()
claims = [claim(i) for i in raw]

matrix = np.zeros(shape=(1000,1000))

for claim in claims:
    for row in range(claim.xd, claim.xd+claim.x):
        for column in range(claim.yd, claim.yd+claim.y):
            if matrix[row,column]==0:
                matrix[row,column]=claim.id
            else:
                matrix[row,column]=-1

nums = []

for i in matrix:
    for x in i:
        nums.append(int(x))

nums = Counter(nums)

for claim in claims:
    if (claim.x*claim.y) == nums[claim.id]:
        print(claim.id)
