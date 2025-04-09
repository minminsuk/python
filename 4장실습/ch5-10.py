import turtle
import random
t = turtle.Turtle()
turtle.speed(100)
t.shape("turtle")
for _ in range(30):
    rand_num = random.randrange(2)
    if rand_num == 0:
        t.right(90)
        t.forward(50)
    else:
        t.left(90)
        t.forward(50)  
turtle.done()


t.reset()
turtle.speed(100)
t.shape("turtle")
steps = 0
while steps < 30:
    rand_num = random.randrange(2)
    if rand_num == 0:
        t.right(90)
        t.forward(50)
    else:
        t.left(90)
        t.forward(50)
    steps += 1
turtle.done()
