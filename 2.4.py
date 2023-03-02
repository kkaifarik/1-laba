with open('2.4.txt') as file:
    file_s = file.read()
    skob = []
    for i in range(len(file_s)):
        if file_s[i] == "(":
            skob.append(file_s[i])
    print('Количество "(": ', len(skob))
    skob.clear()
    for i in range(len(file_s)):
        if file_s[i] == ")":
            skob.append(file_s[i])
    print('Количество ")": ', len(skob))