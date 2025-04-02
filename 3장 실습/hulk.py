import turtle
screen = turtle.Screen()
t = turtle.Turtle()
def handle_input():
    while True:
        user_input = screen.textinput("Input", "Enter command (f, h, n, 1-9):")
        if user_input == "f":
            t.forward(100)
        elif user_input == "h":
            t.turtlesize(10, 10, 1)  
        elif user_input == "n":
            t.turtlesize(1, 1, 1)  
        elif user_input.isdigit() and 1 <= int(user_input) <= 9:
            size = int(user_input)
            t.turtlesize(size, size, 1) 
        else:
            print("Invalid input. Please enter f, h, n, or a number between 1 and 9.")
handle_input()
turtle.done()