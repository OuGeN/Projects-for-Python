"""
def bublesort(list):
    n=len(list)
    for i in range(n):
        for j in range(0,n-i-1):
            if list[j]>list[j+1]:
             temp=list[j]
             list[j]=list[j+1]
             list[j+1]=temp

list=[4,7,9,5,1,3,8]

bublesort(list)
print(list)
"""

"""
def selectionsort(list):
    n=len(list)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            print( "i=", i, "j=", j )
            if list[min]>list[j]:
             min=j

        list[i],list[min]=list[min],list[i]




list=[4,7,9,5,1,3,8]

selectionsort(list)
print(list)
"""
#InsertionSort
"""
def insertionsort(list):
    n=len(list)
    for i in range(1,n):
     key=list[i]
     j=i-1
    while j>= 0 and key<list[j]:
        list[j+1] = list[j]
        j -= 1
    list[j+1] = key


list=[4,7,9,5,1,3,8]

insertionsort(list)
print(list)
"""



def quicksort(list):
    boyut = len(list)
    if(boyut <= 1):
        return list
    else:
        pivot = list[0]
        buyuk=[i for i in list[1:] if i>pivot]
        kucuk=[i for i in list[1:] if i<=pivot]
    return quicksort(kucuk),[pivot],quicksort(buyuk)

list=[4,7,9,5,1,3,8]
quicksort(list)
print(list)
