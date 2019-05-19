x=input("")
y=[]
for i in x.split(","):
    y.append(i)


for i in y:
    z=int(i)**2
    k=z%10
    if (int(k)==int(i)):
        print(True)
    else:
        print(False)