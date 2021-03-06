# threelines2.py
# Jason Moldan

import turtle


def main():
    #global draw_line, make_gap, t

    def draw_line(t):
        t.lt(90)
        t.fd(200)
        t.bk(200)
        t.rt(90)

    def make_gap(t):
        t.penup()
        t.fd(30)
        t.pendown()

    def draw_3_lines():
        draw_line(t)
        make_gap(t)
        draw_line(t)
        make_gap(t)
        draw_line(t)
        t.penup()
        t.back(60)

    t = turtle.Turtle()
    wn = turtle.Screen()
    draw_3_lines()
    wn.exitonclick()


main()