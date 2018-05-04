# threelines2.py
# Jason Moldan

import turtle

def draw_line(t, height):
    t.lt(90)
    t.fd(height)
    t.bk(height)
    t.rt(90)

def make_gap(moxie, gap):
    moxie.penup()
    moxie.fd(gap)
    moxie.pendown()


moxie = turtle.Turtle()
wn = turtle.Screen()


def draw_3_lines(moxie, height, gap):
    draw_line(moxie, height)
    make_gap(moxie, gap)
    draw_line(moxie, height)
    make_gap(moxie, gap)
    draw_line(moxie, height)
    moxie.penup()
    moxie.back(2*gap)


draw_3_lines(moxie, 200, 30)

############# NEED TO FINISH THIS - Make Main Method......

wn.exitonclick()

