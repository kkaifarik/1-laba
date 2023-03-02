with open('books.txt') as FileName:
    data = FileName.readlines()
    print("Список до сортировки:")
    for i in range(len(data)):
        print(data[i], end="")
    print()
    print("Список после сортировки:")
    print()
    for i in range(0, len(data)):
        data[i] = data[i].rstrip("\n")
    data.sort()
    for i in range(len(data)):
        print(data[i], end="\n")
