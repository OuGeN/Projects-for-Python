from functools import reduce
"""
# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(alphabet in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, alphabets)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)
"""
"""
a=range(11)
def ekle(x):
	return x*x
y=map(ekle,a)
print(list(y))
"""

"""
a=range(11)
def topla(x,y): return x+y
print(reduce(topla,a))
"""


s="Işıklı, aydınlık bir bahar günü, bir su kenarında daha yeni göğermiş çimleri iştahla yiyen keçiler gördüm."
print(s)
y=s.replace(',','')
print(y)
z=y.replace('.','')
print(z)
x=z.split(" ")
for i,k in enumerate(x):
    print (i,"=",k,sep="")
