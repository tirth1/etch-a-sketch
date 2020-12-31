from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def go_forward():
    t.forward(10)


def go_backward():
    t.backward(10)


def turn_left():
    new = t.heading() + 10
    t.setheading(new)


def turn_right():
    new = t.heading() - 10
    t.setheading(new)


def counter_clk():
    t.circle(-100, extent=50)


def clk():
    t.circle(100, extent=50)


def clr():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


def speed_up():
    sp = t.speed()
    if sp == 1:
        t.speed(3)
    elif sp == 3:
        t.speed(6)
    elif sp == 6:
        t.speed(10)
    elif sp == 10:
        t.speed(0)


def speed_down():
    sp = t.speed()
    if sp == 3:
        t.speed(1)
    elif sp == 6:
        t.speed(3)
    elif sp == 10:
        t.speed(6)
    elif sp == 0:
        t.speed(10)


def penup():
    t.penup()
    

def pendown():
    t.pendown()
    
    
def do_undo():
    t.undo()


if __name__ == '__main__':
    screen.listen()
    screen.onkeypress(fun=go_forward, key="w")
    screen.onkeypress(fun=go_backward, key="s")
    screen.onkeypress(fun=turn_left, key="a")
    screen.onkeypress(fun=turn_right, key="d")
    screen.onkeypress(fun=clr, key="c")
    screen.onkeypress(fun=speed_up, key="Right")
    screen.onkeypress(fun=speed_down, key="Left")
    screen.onkeypress(fun=penup, key="Up")
    screen.onkeypress(fun=pendown, key="Down")
    screen.onkeypress(fun=do_undo, key="z")
    screen.onkeypress(fun=counter_clk, key="<")
    screen.onkeypress(fun=clk, key=">")
    screen.exitonclick()
