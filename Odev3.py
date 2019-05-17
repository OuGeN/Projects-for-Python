#Bu program oguzhan tarafından kodlanmıştır.


import random
dizi=[]
bir=0
iki=0
uc=0
dort=0
bes=0
alti=0
yedi=0
sekiz=0
dokuz=0



for i in range(100):
    dizi.append(random.randint(1,9))
for j in dizi:
        kactane = [ bir, iki, uc, dort, bes, alti, yedi, sekiz, dokuz ]
        if(j==1):
            bir+=1
        elif(j==2):
            iki+=1
        elif (j == 3):
            uc += 1

        elif (j == 4):
            dort += 1

        elif (j == 5):
            bes += 1
        elif (j == 6):
            alti += 1

        elif (j == 7):
            yedi += 1
        elif (j == 8):
            sekiz += 1

        elif (j == 9):
            dokuz += 1
print(dizi)
print("Bir:",kactane[0],"\nIkı:",kactane[1],"\nUc:",kactane[2],"\nDort:",kactane[3],"\nBes:",kactane[4],"\nAlti:",kactane[5],"\nYedi:",kactane[6],"\nSekiz:",kactane[7],"\nDokuz:",kactane[8])