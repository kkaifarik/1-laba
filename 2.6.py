with open('stek.txt') as files:
    file_s = files.read().split(" ")
    file_s = "".join(file_s)
    stek = []
    for i in range(len(file_s)):
        if file_s[i].isdigit():
            stek.append(file_s[i])
    for i in range(len(file_s)):
        if file_s[i].isalpha():
            stek.append(file_s[i])
    for i in range(len(file_s)):
        if file_s[i].isalnum() == False:
            stek.append(file_s[i])
    file_s = "".join(stek)
    print(file_s)
