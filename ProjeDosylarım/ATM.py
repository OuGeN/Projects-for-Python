x=input("")
y=[]
for i in x.split(","):
    y.append(i)
for i in y:

    if(len(i)==4 or len(i)==6):
        if(i.isdigit()==True):
            print(True)
        else:
            print(False)
    else:
        print(False)
