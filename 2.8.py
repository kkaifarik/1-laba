from collections import deque
with open('2.8.txt') as fil:
    file = fil.readlines()
    coll = deque([1, 2, 3, 4, 5, 6])

    for i in range(0, len(file)):
        file[i] = file[i].rstrip("\n")
    print(file)

    a = 1

    for i in range(0, 3):
        insert = file[len(file)-a]
        coll.insert(len(file)-a, file[i])
        coll.insert(i, insert)
        a += 1
    print(coll)
    for i in range(len(file)):
        print(coll[i], end="\n")
