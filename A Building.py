from turtle import *

speed(0)
bgcolor("black")

penup()
goto(0, 20)
pendown()
color("saddlebrown")
begin_fill()
circle(100)
end_fill()

penup()
goto(-200, -200)
pendown()
begin_fill()
for i in range(2):
    forward(400)
    left(90)
    forward(20)
    left(90)
end_fill()

penup()
goto(-175, -180)
pendown()
color("chocolate")
begin_fill()
for i in range(2):
    forward(350)
    left(90)
    forward(20)
    left(90)
end_fill()

penup()
goto(-150, -160)
pendown()
color("sandybrown")
begin_fill()
for i in range(2):
    forward(300)
    left(90)
    forward(250)
    left(90)
end_fill()

penup()
goto(-175, 90)
pendown()
color("chocolate")
begin_fill()
for i in range(2):
    forward(350)
    left(90)
    forward(20)
    left(90)
end_fill()

penup()
goto(-150, 110)
pendown()
color("sienna")
begin_fill()
for i in range(2):
    forward(300)
    left(90)
    forward(20)
    left(90)
end_fill()

x = -125
y = 30
color("khaki")

def window():
    global x
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    for i in range(4):
        forward(40)
        left(90)
    end_fill()

    x = x + 70

for i in range(3):
    for i in range(4):
        window()
    x = -125
    y = y - 85

hideturtle()
