def lineersearch(list,aranan):

 for i in range(len(list)):
     if list[i]==aranan:
         return (i,list[i])
 else:
     return "False"

list=[15,1,26,35,21,45,55,36,17]
print(lineersearch(list,17))
