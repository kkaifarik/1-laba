tel = input("Введите номер телефона: ")
# FIO = input("Введите ваше ФИО: ")


def prov(tel):
    if tel[0] == "+":
        return tel[1:len(tel)-1].isdigit()
    else:
        return tel[0:len(tel)-1].isdigit()


def provtel(tel):
    if prov(tel) == True and tel[0] == "+" and len(tel) == 12:
        nomtel = '{one}-{two}-{three}-{four}-{five}'.format(
            one=tel[0:2], two=tel[2:5], three=tel[5:8], four=tel[8:10], five=tel[10:])
        print("Ваш номер телефона:", nomtel)
    if prov(tel) == True and tel[0] != "+" and len(tel) == 11:
        nomtel = '{one}-{two}-{three}-{four}-{five}'.format(
            one=tel[0], two=tel[1:4], three=tel[4:7], four=tel[7:9], five=tel[9:])
        print("Ваш номер телефона:", nomtel)
    if prov(tel) == False:
        print("неверный номер телефона, введите в формате (+7/8 (---) (---) (--) (--))")


provtel(tel)
# '{one}-{two}-{three}'.format(two=2, one=1, three=3)
