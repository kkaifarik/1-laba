from collections import deque
with open('kvad_skob.txt') as file:
    file_s = file.read()
    skob = deque([])
    for i in range(len(file_s)):
        if file_s[i] == "[" or file_s[i] == "]":
            skob.append(file_s[i])
    print('Количество "[": ', skob.count('['))
    print('Количество "]": ', skob.count(']'))
