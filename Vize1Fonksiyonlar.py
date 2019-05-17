"""
def StringCevir(kelime):
    kelime.split(",")
    return print(kelime[::-1])





StringCevir("Selam,Naber,Canım")
"""
class Quiz:
    def __init__(self,x=3):
        self.x=x
        print(self.x)
        self.Hesapla()
    def Hesapla(self):
        self.h=self.x**2
        print(self.h)
    def __del__(self):
        print("Finish")
q=Quiz(2)
q.Hesapla()
del(q)
