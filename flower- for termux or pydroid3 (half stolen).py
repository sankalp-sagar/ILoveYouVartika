from math import *

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)
        
def heart():
    turtle.fillcolor('red')
    turtle.begin_fill()
  
    turtle.left(140)
    turtle.forward(113)
  
    curve()
    turtle.left(120)
  
    curve()
  
    turtle.forward(112)
  
    turtle.end_fill()
    
def txt():
    turtle.up()
    turtle.setpos(-68, 380)
    turtle.down()
    turtle.color('lightgreen')
    turtle.write("     Vartika", font=(
      "Verdana", 6, "bold"))
      
x=int(1)
if x == 1:
	import turtle
	from turtle import *
	turtle.penup()
	turtle.left(90)
	turtle.fd(200)
	turtle.pendown()
	
	turtle.right(90)
	
	#base
	
	turtle.fillcolor("red")
	turtle.begin_fill()
	
	turtle.circle(10,180)
	turtle.circle(25,110)
	turtle.left(50)
	turtle.circle(60,45)
	turtle.circle(20,170)
	turtle.right(24)
	turtle.fd(30)
	turtle.left(10)
	turtle.circle(30,110)
	turtle.fd(20)
	turtle.left(40)
	turtle.circle(90,70)
	turtle.circle(30,150)
	turtle.right(30)
	turtle.fd(15)
	turtle.circle(80,90)
	turtle.left(15)
	turtle.fd(45)
	turtle.right(165)
	turtle.fd(20)
	turtle.left(155)
	turtle.circle(150,80)
	turtle.left(50)
	
	turtle.circle(150,90)
	turtle.end_fill()
	
	#pt1
	
	turtle.left(150)
	turtle.circle(-90,70)
	turtle.left(20)
	turtle.circle(75,105)
	turtle.setheading(60)
	turtle.circle(80,98)
	turtle.circle(-90,40)
	
	#pt2
	turtle.left(180)
	turtle.circle(90,40)
	turtle.circle(-80,98)
	turtle.setheading(-83)
	
	#leaves
	turtle.fd(30)
	turtle.left(90)
	turtle.fd(25)
	turtle.left(45)
	turtle.fillcolor("green")
	turtle.begin_fill()
	
	turtle.circle(-80,90)
	turtle.right(90)
	
	turtle.circle(-80,90)
	turtle.end_fill()
	
	turtle.right(135)
	turtle.fd(60)
	turtle.left(180)
	turtle.fd(85)
	turtle.left(90)
	turtle.fd(80)
	
	#leaves2
	
	turtle.right(90)
	turtle.right(45)
	turtle.fillcolor("green")
	turtle.begin_fill()
	
	turtle.circle(80,90)
	turtle.left(90)
	turtle.circle(80,90)
	turtle.end_fill()
	
	turtle.left(135)
	turtle.fd(60)
	turtle.left(180)
	turtle.fd(60)
	turtle.right(90)
	turtle.circle(200,60)
	color("red")
	
	#V
	turtle.penup()
	turtle.setpos(-320,-350)
	turtle.setheading(270)
	turtle.pendown()
	turtle.left(20)
	forward(sqrt(120*2 + 20*2))
	left(140)
	forward(sqrt(120*2 + 20*2))
	right(160)
	color("white")
	forward(120)
	left(90)
	forward(20)
	color("red")
	
	#A.. had to stop at half on second
	left(70)
	forward(sqrt(120*2 + 20*2))
	right(140)
	forward((sqrt(120*2 + 20*2))/2)
	right(110)
	forward(40)
	back(40)
	left(110)
	forward((sqrt(120*2 + 20*2))/2)
	left(70)
	color("white")
	forward(40)
	color("red")
	left(90)
	
	#R
	forward(120)
	right(90)
	forward(60)
	right(90)
	forward(60)
	right(90)
	forward(60)
	left(135)
	forward(sqrt(60*2 + 60*2))
	left(45)
	color("white")
	forward(70)
	left(90)
	color("red")
	
	#T
	forward(120)
	left(90)
	forward(30)
	back(60)
	right(180)
	color("white")
	forward(40)
	color("red")
	right(90)
	
	#I
	forward(120)
	left(90)
	color("white")
	forward(40)
	left(90)
	color("red")
	
	#K
	forward(120)
	back(60)
	right(45)
	forward(sqrt(7200))
	back(sqrt(7200))
	right(90)
	forward(sqrt(7200))
	left(45)
	color("white")
	forward(40)
	color("red")
	
	#A.. had to stop at half on second
	left(70)
	forward(sqrt(120*2 + 20*2))
	right(140)
	forward((sqrt(120*2 + 20*2))/2)
	right(110)
	forward(40)
	back(40)
	left(110)
	forward((sqrt(120*2 + 20*2))/2)
	left(70)
	color("white")
	forward(20)
	turtle.penup()
	
	#for heart
	
	turtle.setpos(0,300)
	pendown()
	color("red")
	heart()
	txt()
	turtle.ht()
	turtle.done()