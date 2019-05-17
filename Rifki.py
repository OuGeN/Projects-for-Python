#!/usr/bin/env python
# -*- coding: utf-8 -*-
kucuk="abcçdefgğhıijklmnoöprsştuüvyz"
buyuk="ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"

girdi=input().split(",")
print(girdi)
print(len(girdi))

for i in range(len(girdi)):
    toplam=0
    for j in range(len(girdi[i])):
        gecici=girdi[i][::1]
        if(gecici.isupper()==True):
            toplam+=toplam+(buyuk.index(gecici)*3+60)

        else:
            toplam=toplam+(kucuk.index(gecici)+kucuk.index(gecici)+1)



    if(toplam%13==0):
        print("True")

    else:
          print("False")



#dizi.append(girdi.split(","))
toplam=0

