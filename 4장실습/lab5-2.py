import turtle
t = turtle.Turtle()
t.shape("turtle")
count = 0
while count < 3:
    t.forward(100)
    t.left(360/3)
    count += 1

t.penup()
t.goto(200, 0)
t.pendown()

count = 0
while count < 4:
    t.forward(100)
    t.left(360/4)
    count += 1
