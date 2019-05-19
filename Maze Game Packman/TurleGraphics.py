from turtle import*
wn=Turtle.Screen()
wn.shape("turtle")
wheel=12
wn.bgcolor("blue")
wn.pensize(10)
wn.pencolor("red")

for i in range(wheel):
    wn.begin_fill();wn.rt(90);wn.fd(200);wn.end_fiil()
    wn.fd(200)