import turtle

t = turtle.Turtle()
t.shape("turtle")
base = 100
height = 100

t.forward(base)  
t.left(90)
t.forward(height) 
t.left(135)
t.forward((base**2 + height**2)**0.5)  

turtle.done()