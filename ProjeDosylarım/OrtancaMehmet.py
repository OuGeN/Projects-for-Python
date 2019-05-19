girdi=input("")

x=girdi.split(",")

for i in x:
    if(len(i)%2!=0):
        f=len(i)//2
        print(i[f])
    else:
        f1=(len(i)//2)-1
        f2=len(i)//2
        print(i[f1]+i[f2])