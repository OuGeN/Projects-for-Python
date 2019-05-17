
def minimumNumber(n):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

passwordlist=list()
for a in range(0,100):
 number=0
 lower=0
 upper=0
 special=0
 password=str(input(""))
 count=len(password)
 if(count==8):
  for i in range(0,count):

    parca=password[i:i+1]
    if(parca.isupper()==True):
        upper+=1
    elif(parca.islower()==True):
        lower+=1
    elif(parca.isnumeric()==True):
        number+=1
    else:
     special+=1
  if(upper>0 and lower>0 and number>0 and special>0 ) :
    print("Pass Dogru Listeye eklendi")
    passwordlist.append(password)
  else:
   print("Pass Yanlıs")
   a-=1
 else:
    print("8 karekter giriniz lütfen")




"""
liste=list()

for i in range(1,100):
    passw=input("Bir sifre girin:")
     if():
     liste.append(i)
"""