from collections import deque
with open('chisla.txt') as filess:
    file = filess.read().split(" ")
    chisla = deque([])
    for i in range(0, len(file)):
        if i == len(file)-1:
            file[i] = file[i].rstrip(".")
        else:
            file[i] = file[i].rstrip(",")
    for i in range(0, len(file)):
        if int(file[i]) < 0:
            chisla.appendleft(int(file[i]))
        else:
            chisla.append(int(file[i]))
    print(chisla)
