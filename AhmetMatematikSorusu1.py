#!/bin/python

"""
ougen
"""



import string
from random import *
dizi=[]
harfler = string.ascii_letters
sayilar = string.digits
semboller = string.punctuation
karakterler = harfler+sayilar+semboller
min_uzunluk = 8
max_uzunluk = 8
boyut=len(dizi)
f=open("Sifreler.txt","w")
for i in range(0,100):
  sifre = "".join(choice(karakterler)
   for x in range(randint(min_uzunluk, max_uzunluk)))
  dizi.append(sifre)

print(dizi)

for k in dizi:
    kelime=k
    for j in range(len(k)-1):
        if (k[j].isdigit() and k[j+1].isdigit()):
         f.write(kelime)
         print("\033[1;31;40m",k)

f.close()
