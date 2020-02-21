import turtle
import time
import random

money1 = 50
t = 0

wn = turtle.Screen()
wn.title("Race")
wn.bgcolor("green")
wn.setup(height=700,width=700)
wn.tracer(0)


#pen
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.goto(-120,250)
pen.color("white")
pen.write("Turetle Race", font=("ariel",30,"bold"))




#money
money = turtle.Turtle()
money.penup()
money.goto(-325,250)
money.color("white")
money.write("Money:  {} ".format(money1),font=("ariel",15,"bold"))
money.clear()
money.hideturtle()

#dirt
dirt = turtle.Turtle()
dirt.color("chocolate")
dirt.penup()
dirt.goto(-390,-360)
dirt.begin_fill()
dirt.pendown()
dirt.forward(800)
dirt.left(90)
dirt.forward(200)
dirt.left(90)
dirt.forward(950)
dirt.left(90)
dirt.forward(200)
dirt.end_fill()
dirt.hideturtle()

#finish line
stamp_size = 20
square_size = 15
finis_line = 200

finisline = turtle.Turtle()
finisline.color("black")
finisline.shape("square")
finisline.penup()

for i in range(10):
    finisline.setpos(finis_line, (180 - (i * square_size * 2)))
    finisline.stamp()

for j in range(10):
    finisline.setpos(finis_line + square_size, ((180 - square_size) - (j * square_size * 2)))
    finisline.stamp()


#turtle 1
turtle1 = turtle.Turtle()
turtle1.speed(0)
turtle1.color("black")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-250,150)

#turtle 2
turtle2 = turtle.Turtle()
turtle2.speed(0)
turtle2.color("cyan")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-250,100)

#turtle 3
turtle3 = turtle.Turtle()
turtle3.speed(0)
turtle3.color("yellow")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-250,50)

#turtle 4
turtle4 = turtle.Turtle()
turtle4.speed(0)
turtle4.color("red")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-250,0)

#turtle 5
turtle5 = turtle.Turtle()
turtle5.speed(0)
turtle5.color("magenta")
turtle5.shape("turtle")
turtle5.penup()
turtle5.goto(-250,-50)



bet = input("who will win?")
hm = int(input("how much?"))
if hm > money1:
    while hm > money1:
        print("you dont have einaf money!")
        hm = int(input("how much?"))
money1 -= hm


while True:
    wn.update()
    time.sleep(0.05)
    for l in range(1):
        turtle1.forward(random.randint(1,5))
        turtle2.forward(random.randint(1,5))
        turtle3.forward(random.randint(1,5))
        turtle4.forward(random.randint(1,5))
        turtle5.forward(random.randint(1,5))
    money.write("Money:  {} ".format(money1), font=("ariel", 15, "bold"))
    if turtle1.distance(200,150) < 20:
        turtle5.goto(-250, -50)
        turtle4.goto(-250, 0)
        turtle3.goto(-250, 50)
        turtle2.goto(-250, 100)
        winner = "black"
        # pen
        pen1 = turtle.Turtle()
        pen1.penup()
        pen1.hideturtle()
        pen1.goto(-100, 175)
        pen1.color("white")
        pen1.write("{}".format(winner), font=("ariel", 20, "bold"))
        money.write("Money:  {} ".format(money1), font=("ariel", 15, "bold"))
        money.clear()
        time.sleep(2)
        pen1.clear()
        turtle1.goto(-250,150)
        turtle1.clear()
        turtle2.clear()
        turtle3.clear()
        turtle4.clear()
        turtle5.clear()
        if bet == winner:
            money1 = money1 + hm * 2
        bet = input("who will win?")
        hm = int(input("how much?"))
        if hm > money1:
            while hm > money1:
                print("you dont have enough money!")
                hm = int(input("how much?"))
        money1 -= hm
        time.sleep(3)
    if turtle2.distance(200,100) < 20:
        turtle5.goto(-250, -50)
        turtle4.goto(-250, 0)
        turtle3.goto(-250, 50)
        turtle1.goto(-250, 150)
        winner = "cyan"
        # pen
        pen1 = turtle.Turtle()
        pen1.penup()
        pen1.hideturtle()
        pen1.goto(-100, 175)
        pen1.color("white")
        pen1.write("{}".format(winner), font=("ariel", 20, "bold"))
        money.write("Money:  {} ".format(money1), font=("ariel", 15, "bold"))
        money.clear()
        time.sleep(2)
        pen1.clear()
        turtle2.goto(-250,100)
        turtle1.clear()
        turtle2.clear()
        turtle3.clear()
        turtle4.clear()
        turtle5.clear()
        if bet == winner:
            money1 += hm * 2
        bet = input("who will win?")
        hm = int(input("how much?"))
        if hm > money1:
            while hm > money1:
                print("you dont have enough money!")
                hm = int(input("how much?"))
        money1 -= hm
        time.sleep(3)
    if turtle3.distance(200,50) < 20:
        turtle5.goto(-250, -50)
        turtle4.goto(-250, 0)
        turtle1.goto(-250, 150)
        turtle2.goto(-250, 100)
        winner = "yellow"
        # pen
        pen1 = turtle.Turtle()
        pen1.penup()
        pen1.hideturtle()
        pen1.goto(-100, 175)
        pen1.color("white")
        pen1.write("{}".format(winner), font=("ariel", 20, "bold"))
        money.write("Money:  {} ".format(money1), font=("ariel", 15, "bold"))
        money.clear()
        time.sleep(2)
        pen1.clear()
        turtle3.goto(-250,50)
        turtle1.clear()
        turtle2.clear()
        turtle3.clear()
        turtle4.clear()
        turtle5.clear()
        if bet == winner:
            money1 += hm * 2
        bet = input("who will win?")
        hm = int(input("how much?"))
        if hm > money1:
            while hm > money1:
                print("you dont have enough money!")
                hm = int(input("how much?"))
        money1 -= hm
        time.sleep(3)
    if turtle4.distance(200,0) < 20:
        turtle5.goto(-250, -50)
        turtle1.goto(-250, 150)
        turtle3.goto(-250, 50)
        turtle2.goto(-250, 100)
        winner = "red"
        # pen
        pen1 = turtle.Turtle()
        pen1.penup()
        pen1.hideturtle()
        pen1.goto(-100, 175)
        pen1.color("white")
        pen1.write("{}".format(winner), font=("ariel", 20, "bold"))
        money.write("Money:  {} ".format(money1), font=("ariel", 15, "bold"))
        money.clear()
        time.sleep(2)
        pen1.clear()
        turtle4.goto(-250,0)
        turtle1.clear()
        turtle2.clear()
        turtle3.clear()
        turtle4.clear()
        turtle5.clear()
        if bet == winner:
            money1 += hm * 2
        bet = input("who will win?")
        hm = int(input("how much?"))
        if hm > money1:
            while hm > money1:
                print("you dont have enough money!")
                hm = int(input("how much?"))
        money1 -= hm
        time.sleep(3)
    if turtle5.distance(200,-50) < 20:
        turtle1.goto(-250, 150)
        turtle4.goto(-250, 0)
        turtle3.goto(-250, 50)
        turtle2.goto(-250, 100)
        winner = "pink"
        # pen
        if turtle5 == (0,-50):
            turtle5.left(100)
        pen1 = turtle.Turtle()
        pen1.penup()
        pen1.hideturtle()
        pen1.goto(-100, 175)
        pen1.color("white")
        pen1.write("{}".format(winner), font=("ariel", 20, "bold"))
        money.write("Money:  {} ".format(money1), font=("ariel", 15, "bold"))
        money.clear()
        time.sleep(2)
        pen1.clear()
        turtle5.goto(-250,-50)
        turtle1.clear()
        turtle2.clear()
        turtle3.clear()
        turtle4.clear()
        turtle5.clear()
        if bet == winner:
            money1 += hm * 2
        bet = input("who will win?")
        hm = int(input("how much?"))
        if hm > money1:
            while hm > money1:
                print("you dont have enough money!")
                hm = int(input("how much?"))
        money1 -= hm
        time.sleep(3)
wn.mainloop()


