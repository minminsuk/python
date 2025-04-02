import turtle
t = turtle.Turtle()
for _ in range(3):
    t.forward(100)
    t.left(120)
    for _ in range(2):
        t.forward(100)
        t.left(120)
    for _ in range(5):
        t.forward(100)
        t.left(120)
    for _ in range(4):
        t.forward(100)
        t.left(120)
turtle.done()
