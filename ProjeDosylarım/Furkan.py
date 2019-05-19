x=input("")
y=[]
z=[]
for i in x.split("|"):
    y.append(i)
for j in y:
    z.append(j.split(","))


for i in z:
    if((i[1]=='')):
        if(int(i[2])<10):
            print(i[0])
