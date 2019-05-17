def binarysearch(list,aranan):
 indis=len(list)//2
 if aranan==list[indis]:
     return ()
 elif aranan<list[indis]:
     return list[indis:]
 else:
     return list[:indis]


list=[1,2,3,5,9,10,15,22,35,48,51]
print(binarysearch(list,22))
