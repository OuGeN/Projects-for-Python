girdi=input("")

x=girdi.split(" ")
liste1=[]
liste2=[]
for i in x:
    if(i[0].isupper()):
       liste1.append(i)
    else:
        liste2.append(i)

liste3=liste1+liste2
for i in liste3:
    print(i,end=" ")
