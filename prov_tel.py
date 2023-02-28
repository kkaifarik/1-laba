tel=input("Введите номер телефона: ")
def prov(args):
    if tel[0]=="+":
        tel_prov=tel[1:len(tel)-1]
        return tel_prov.isdigit()
    else:
        return tel[0:len(tel)-1].isdigit()
if prov(True) and tel[0]=="+" and len(tel)==12:
    print("Ваш номер телефона:",'{one}-{two}-{three}-{four}-{five}'.format(one=tel[0:2],two=tel[2:5],three=tel[5:8],four=tel[8:10],five=tel[10:]))
if prov(True) and tel[0]!="+" and len(tel)==11:
    print("Ваш номер телефона:",'{one}-{two}-{three}-{four}-{five}'.format(one=tel[0],two=tel[1:4],three=tel[4:7],four=tel[7:9],five=tel[9:]))
else:
    print("неверный номер телефона, введите в формате (+7/8 (---) (---) (--) (--))")
#'{one}-{two}-{three}'.format(two=2, one=1, three=3)    