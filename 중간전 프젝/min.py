from turtle import TurtleScreen, RawTurtle, TK

def main():
    root = TK.Tk()
    cv1 = TK.Canvas(root, width=300, height=200, bg="#ddffff")
    cv2 = TK.Canvas(root, width=300, height=200, bg="#ffeeee")
    cv1.pack()
    cv2.pack()

    s1 = TurtleScreen(cv1)
    s1.bgcolor(0.5, 0.5, 1)
    s2 = TurtleScreen(cv2)
    s2.bgcolor(1, 0.5, 0.5)

    p = RawTurtle(s1)
    q = RawTurtle(s2)

    p.color("black")
    p.width(3)
    q.color("white")
    q.width(3)

    for t in p, q:
        t.shape("turtle")
        t.penup()

    p.goto(-50, 0)
    q.goto(-50, 0)

    # Writing "민" on cv1 using p (RawTurtle)
    p.write("민", font=("Arial", 48, "normal"))
    # Writing "석" on cv2 using q (RawTurtle)
    q.write("석", font=("Arial", 48, "normal"))

    return "EVENTLOOP"


if __name__ == '__main__':
    main()
    TK.mainloop()  # keep window open until user closes it
