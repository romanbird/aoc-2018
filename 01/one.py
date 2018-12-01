raw = open("input.txt").readlines()
count=0
for i in raw:
    count+=int(i.strip())
print(count)
