import turtle
import random
t = turtle.Turtle()
t.shape("turtle")
t.speed(1)
for _ in range(10):
    rand_num = random.randrange(2)
    if rand_num == 0:
        t.right(90)
        t.forward(50)
    else:
        t.left(90)
        t.forward(50)  
turtle.done()
