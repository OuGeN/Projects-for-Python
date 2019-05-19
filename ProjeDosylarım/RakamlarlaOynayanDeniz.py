x=input("")
y=[]
for i in x.split(","):
    y.append(i)

print(y)
for i in y:
    for j in range(len(i)-1):
        if (i[ j ] <= i[ j + 1 ]):
            i[j],i[j+1]=i[j+1],i[j]
            print(j[i])
    else:
        print(-1)

