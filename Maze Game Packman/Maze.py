import turtle
import math
import random
import sys

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Yaptigim Ilk Oyun")
wn.setup(700,700)
wn.tracer(0)

resimler=["wall.gif","pacman.gif","pacmansol.gif",
        "enemyright.gif","enemyleft.gif"]
for resim in resimler:
    turtle.register_shape(resim)
#Pencere Olustur
class Pencere(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
class Oyuncu(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("pacman.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold=0

    def yukari(self):
        move_to_x=oyuncu.xcor()
        move_to_y=oyuncu.ycor()+24
        if(move_to_x,move_to_y) not in duvar:
            self.goto(move_to_x,move_to_y)
    def alta(self):
        move_to_x = oyuncu.xcor()
        move_to_y = oyuncu.ycor()-24
        if (move_to_x, move_to_y) not in duvar:
            self.goto(move_to_x, move_to_y)
    def sol(self):
        move_to_x = oyuncu.xcor()-24
        move_to_y = oyuncu.ycor()
        self.shape("pacmansol.gif")
        if (move_to_x, move_to_y) not in duvar:
            self.goto(move_to_x, move_to_y)

    def sag(self):
        move_to_x = oyuncu.xcor()+24
        move_to_y = oyuncu.ycor()
        self.shape("pacman.gif")
        if (move_to_x, move_to_y) not in duvar:
            self.goto(move_to_x, move_to_y)

    def carpisma(self,other):
        a=self.xcor()-other.xcor()
        b=self.ycor()-other.ycor()
        mesafe=math.sqrt((a**2)+(b**2))
        if mesafe<5:
            return True
        else:
            return False

class Hazine(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold=50
        self.goto(x,y)
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
class Dusman(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("enemyleft.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold=25
        self.goto(x,y)
        self.direction=random.choice(["up","down","right","left"])
    def hareket(self):
        if self.direction=="up":
            dx=0
            dy=24
        elif self.direction=="down":
            dx=0
            dy=-24
        elif self.direction=="left":
            dx=-24
            dy=0
            self.shape("enemyleft.gif")
        elif self.direction=="right":
            dx=24
            dy=0
            self.shape("enemyright.gif")
        else:
            dx=0
            dy=0


        if self.yakin(oyuncu):
            if oyuncu.xcor()<self.xcor():
                self.direction="left"
            elif oyuncu.xcor()>self.xcor():
                self.direction="right"
            elif oyuncu.ycor()<self.ycor():
                self.direction="down"
            elif oyuncu.ycor()>self.ycor():
                self.direction="up"

        #Hesaplayici olustur
        move_to_x=self.xcor()+dx
        move_to_y=self.ycor()+dy

        #Kontrol et
        if(move_to_x,move_to_y)not in duvar:
            self.goto(move_to_x,move_to_y)
        else:
            self.direction=random.choice(["up","down","right","left"])

        #Zamanlayıcı
        turtle.ontimer(self.hareket,t=random.randint(100,300))

    def yakin(self,other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        mesafe = math.sqrt( (a ** 2) + (b ** 2))
        if mesafe<75:
            return True
        else:
            return False
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

#Level Listesi Olustur
levels=['']

#Birinci leveli tanımla
level_1=[
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXX          XXXXX",
"X  XXXXXXX  XXXXX   XXXXX",
"X       XX  XXXXX   XXXXX",
"X       XX  XXX       EXX",
"XXXXXX  XX  XXX        XX",
"XXXXXX  XX  XXXXX   XXXXX",
"XXXXXX  XX   XXXX   XXXXX",
"X  XX        XXXXT  XXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"X                XXXXXXXX",
"XXXXXXXXXXXX     XXXXX  X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX  XXXXXXXXXX         X",
"XXXE                   TX",
"XXX         XXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX             TX",
"XX  TXXXXX              X",
"XX   XXXXXXXXXXXXXE XXXXX",
"XX    YXXXXXXXXXXX  XXXXX",
"XX         TXXXX        X",
"XXXXE                   X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]
#Hazine ekleyelim
hazine_listesi= []

#Dusman listesi olusturalım
dusmanlar=[]

#Buraya listemizi ekleyelim
levels.append(level_1)

#Level atlama fonskiyonu olusturalım
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #Her x, y koordinatindaki karakteri al
            #Satirlara dikkat edin y ve x kordinatlarindaki
            charecter =level[y][x]
            #X ve Y kordinatlari hesabi yapalim.
            screen_x= -288+(x*24)
            screen_y= 288-(y*24)

            #Eger temsil eden X i kontrol et
            if charecter=="X":
                pen.goto(screen_x,screen_y)
                pen.shape("wall.gif")
                pen.stamp()
                #Duvari x kordinatlarına ekliyoruz
                duvar.append((screen_x,screen_y))
            if charecter=="P":
                oyuncu.goto(screen_x,screen_y)
            if charecter=="T":
                hazine_listesi.append(Hazine(screen_x,screen_y))
            if charecter=="E":
                dusmanlar.append(Dusman(screen_x,screen_y))

#Class in nesnesini olusturuyoruz
pen= Pencere()
oyuncu=Oyuncu()

#Duvar olusturalım
duvar=[]

#Leveli fonksiyona atma
setup_maze(levels[1])
print(duvar)


#Klavye girdisi
turtle.listen()
turtle.onkey(oyuncu.sol,'Left')
turtle.onkey(oyuncu.sag,'Right')
turtle.onkey(oyuncu.yukari,'Up')
turtle.onkey(oyuncu.alta,'Down')

#Update i durdurur
wn.tracer(0)

#Burasi çok önemli
for dusman in dusmanlar:
    turtle.ontimer(dusman.hareket,t=250)

while True:
    #Carpismayi kontrol et
    for hazine in hazine_listesi:
        if oyuncu.carpisma(hazine):
            oyuncu.gold+=hazine.gold
            print("Oyuncunun Toplam Altini:{}".format(oyuncu.gold))
            #Hazineyi yıkmalıyız
            hazine.destroy()
            #yok etmeliyiz aldıktan sonra
            hazine_listesi.remove(hazine)
    #Olumu kontrol et
    for dusman in dusmanlar:
        if oyuncu.carpisma(dusman):
            sys.exit(print("Oyuncu Kaybetti"))

        else:
            continue

#Burada tekrar güncelleme olucak
    wn.update()
