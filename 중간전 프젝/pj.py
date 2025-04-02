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

    p.color("black", (1, 0.85, 0.85))
    p.width(3)
    q.color("white", (0.85, 0.85, 1))
    q.width(3)

    for t in p,q:
        t.shape("turtle")
        t.lt(36)

    q.lt(180)
    for i in range(5):
        for t in p, q:
            t.fd(100)
            t.rt(144)
   

    return "EVENTLOOP"


if __name__ == '__main__':
    main()
    TK.mainloop()  # keep window open until user closes it


