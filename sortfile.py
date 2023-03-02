name = input("Как вас зовут? ")
# Name=name.title()
with open("split.txt", "r") as str1:
    # str1="я? все? хочу? быть? умным?"
    str1 = str1.read().split(" ")
    for i in range(len(str1)-1):
        if i == 0:
            str1[i] = str1[i].title()
            str1[i] = str1[i].rstrip("?")
        else:
            str1[i] = str1[i].rstrip("?")
    # str1=str1.lstrip("?")
    str1 = " ".join(str1)
    s = 'пошел на хуй'
    # print(s.center(len(s)+13,'_'))
    str1 = str1 + "\n" + name.title() + "? " + s.center(len(s)+14, '_')
    print(str1)
prov = input()
print("Объект имеет только цифры:", prov.isdigit())
print("Объект имеет только буквы:", prov.isalpha())
print("Объект имеет только цифры и буквы:", prov.isalnum())
print("Объект имеет только буквы:", prov.isnumeric())
