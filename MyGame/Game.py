import turtle as t
import math as m
import random as r
import playsound as ps
wn=t.Screen();
wn.bgcolor("black")
wn.tracer(3)
wn.bgpic("mm.png")
mypen=t.Turtle()
mypen.penup()
mypen.setposition(-263,-260)
mypen.pendown()
mypen.pensize(4)
mypen.color("yellow")
for side in range(4):
    mypen.forward(525)
    mypen.left(90)
mypen.hideturtle()

player=t.Turtle()
player.color("green")
player.shape("turtle")
player.penup()
player.speed(0)
score=0
maxGoals=12
goals=[]
for count in range(maxGoals):
    goals.append(t.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(r.randint(-275,240),r.randint(-250,260))
speed=1
def turnleft():
    player.left(30)
def turnright():
    player.right(30)
def increasespeed():
    global speed
    speed+=1
def isCollision(t1,t2):
    d=m.sqrt(m.pow(t1.xcor()-t2.xcor(),2)+m.pow(t1.ycor()-t2.ycor(),2))
    if d<20:
        return True
    else:
        return False
t.listen()
t.onkey(turnleft,"Left")
t.onkey(turnright,"Right")
t.onkey(increasespeed,"Up")
while True:
    player.forward(speed)
    if player.xcor()>240 or player.xcor()<-265:
        player.right(180)
        #os.system("")
    if player.ycor()>260 or player.ycor()<-240:
        player.right(180)
   
    for count in range(maxGoals):    
        goals[count].forward(1)   

        if goals[count].xcor()>=240 or goals[count].xcor()<=-265:
            goals[count].right(180)

        if goals[count].ycor()>=260 or goals[count].ycor()<=-240:
            goals[count].right(180)

        if isCollision(player,goals[count]):
            goals[count].setposition(r.randint(-265,240),r.randint(-250,260))
            goals[count].right(r.randint(0,360))
            score+=1
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-250,265)
            scorestr="Score %s" %score
            mypen.write(scorestr,False,align="Left" ,font=("Arial",14,"normal"))
            ps.playsound("mail.mp3",True)
