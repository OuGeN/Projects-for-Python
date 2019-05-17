def tamBolen(sayi):
    tamBolenler=[]
    for i in range(1,sayi+1):
        if (sayi % i == 0):
            tamBolenler.append(i)
    return tamBolenler[2]


sayi = int(input(""))
print("",tamBolen(sayi))