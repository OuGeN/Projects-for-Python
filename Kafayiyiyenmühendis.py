def tamBolen(sayi):
    tamBolenler=[]

    for i in range(1,sayi+1):
        if (sayi%i == 0):
            tamBolenler.append(i)
    return tamBolenler[x-1]


sayi, x = map(int, input().split())
print("",tamBolen(sayi))