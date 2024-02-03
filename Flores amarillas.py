import turtle

screen = turtle.Screen()
screen.bgcolor("skyblue")
t = turtle.Turtle()
t.shape("turtle")
t.color("brown")
t.speed(0)

def dibujar_petal(t, radio):
    t.pensize(2)
    t.pencolor("black")
    t.color("yellow")
    t.begin_fill()
    t.circle(radio, 60)
    t.left(120)
    t.circle(radio, 60)
    t.end_fill()
    t.pencolor("brown")
    t.pensize(1)

def dibujar_girasol():
    radio = 100
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.pensize(8)
    t.left(90)
    t.color("green")
    t.forward(180)

    for _ in range(18):
        dibujar_petal(t, radio)
        t.right(20)

    t.penup()
    t.goto(8, 80)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

t.penup()
t.goto(-400, -100)
t.pendown()
t.color("green")
t.begin_fill()
for _ in range(2):
    t.forward(800)
    t.right(90)
    t.forward(200)
    t.right(90)
t.end_fill()

dibujar_girasol()
t.penup()
t.goto(0, 200)
t.color("red")
t.write("Enviarte estas cosas me hace feliz <3", align="center", font=("Arial", 15, "bold"))

t.hideturtle()
turtle.done()