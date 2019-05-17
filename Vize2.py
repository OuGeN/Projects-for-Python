class Personel():
    def __init__(self,isim="Personel",maas=0):
        self.isim=isim
        self.maas=maas
        print(self.__class__.__name__+" olustu.")
    def PersonelBilgisi(self):

        print("İsim:{}\nMaasi:{}".format(self.isim,self.maas))
    def __str__(self):
        return self.__class__.__name__+": "+self.isim+" Maasi:"+str(self.maas)+" Görevi:Yönetici"



class Teknik_personel(Personel):
        def __init__(self,isim="personel",maas=0,gorev=""):
         self.isim=isim
         self.maas=maas
         self.gorev=gorev
         print( self.__class__.__name__ + " olustu")
        def __str__(self):
             return self.__class__.__name__ + ": " + self.isim + " Maasi:" + str( self.maas )+" Görevi:"+self.gorev

oguzhan=Personel("Oguzhan Yesilpinar",10000)
osman=Teknik_personel("Nadire Bay",3000,"Java Devoloper")
print(oguzhan)
print(osman)


