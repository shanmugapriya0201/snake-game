import turtle
import random

w = 500
h = 500
fs = 10
d = 100

off = {"up":(0,20),"down":(0,-20),"left":(-20,0),"right":(20,0)}

def r():
    global sp, ka, kt, pn
    sp = [[0,0], [0,20], [0,40], [0,60], [0,80]]
    ka = "up"
    kt = nun()
    food.goto(kt)
    hall()

def hall():
    global ka
    new_head=sp[-1].copy()
    new_head[0]=sp[-1][0]+off[ka][0]
    new_head[1] = sp[-1][1] + off[ka][1]
    if new_head in sp[:-1]:
        r()
    else:
        sp.append(new_head)
        if not kn():
            sp.pop(0)

        if sp[-1][0]>w/2:
            sp[-1][0]-=w
        elif sp[-1][0]<-w/2:
            sp[-1][0]+=w
        elif sp[-1][1]>h/2:
                sp[-1][1] -= h
        elif sp[-1][1]<-h/2:
                sp[-1][1] += h
        pen.clearstamps()

        for segment in sp:
            pen.goto(segment[0],segment[1])
            pen.stamp()

        screen.update()
        turtle.ontimer(hall,d)

def kn():
    global kt
    if dist(sp[-1],kt)<20:
        kt=nun()
        food.goto(kt)
        return True
    return False

def nun():
    x=random.randint(-w/2+fs, w/2-fs)
    y=random.randint(-h/2+fs, h/2-fs)
    return(x,y)

def dist(pos1,pos2):
    x1,y1=pos1
    x2,y2=pos2
    distance=((y2-y1)**2+(x2-x1)**2)*0.5
    return distance

def ma():
    global ka
    if ka!="down":
         ka="up"

def go_right():
    global ka
    if ka!="left":
        ka="right"

def go_left():
    global ka
    if ka!="right":
        ka="left"

def go_down():
    global ka
    if ka!="up":
        ka="down"

screen=turtle.Screen()
screen.setup(w,h)
screen.title("SNAKEY")
screen.bgcolor("cyan")
screen.setup(500,500)
screen.tracer(0)

pen=turtle.Turtle("square")
pen.penup()

food=turtle.Turtle()
food.shape("circle")
food.color("brown")
food.shapesize(fs/10)
food.penup()

screen.listen()
screen.onkey(ma,"Up")
screen.onkey(go_right,"Right")
screen.onkey(go_down,"Down")
screen.onkey(go_left,"Left")

r()
turtle.done()







