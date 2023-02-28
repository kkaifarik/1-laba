a=[]
b=[]

def coins_1(a):
    print("Введите количество монет с разным номиналом:")
    kol_1=int(input())
    a = [int(input("Введите номинал монеты: {}".format(i))) for i in range(kol_1)]
    a.sort()
    return(a)
def coins_2(b):
    print("Введите количество монет с разным номиналом:")
    kol_2=int(input())
    b = [int(input("Введите номинал монеты: ".format(i))) for i in range(kol_2)]
    b.sort()
    return(b)
print(coins_1(a))
print(coins_2(b))