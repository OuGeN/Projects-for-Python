# -*- coding: UTF-8 -*-
import math
karakterler = ["A", "B", "C", "D", "E", "F", "I", "J", "K", "L", "M", "O", "P", "S", "T", "U", "Y", "Z"]

A=789456123
iter=int(input(""))
sifre=""
for i in range(9, -1, -1):
    temp = int(math.pow(18, i))
    a = iter / temp
    if a > 0:
        sifre += karakterler[a - 1]
print (sifre)












