def Hesapla(x):
    return x*2

liste=list(map(Hesapla,[1,2,3,4,5,6,7]))
print(liste)


liste2=list(map(lambda x:x**2,[1,2,3,4,5,6,7]))
print(liste2)
