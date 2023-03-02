from collections import deque
with open('2.8.txt') as fil:
    file = list(fil.readlines())
coll = deque([])
coll = file[::-1]
for i in range(len(file)):
    coll[i] = coll[i].rstrip("\n")
for i in range(len(file)):
    print(coll[i], end="\n")
