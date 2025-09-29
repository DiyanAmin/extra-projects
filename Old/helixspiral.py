#Helix Spiral - Infinity
import turtle
turtle.Screen().setup
turtle.Screen().bgcolor('light blue')
#Initializing
start=turtle.Turtle()
#Pen colour inti
turtle.pencolor('red')
turtle.speed(100000000)
#Infinitly repeating:-
while True:
 turtle.speed(100000000)
 val=0
 while val<360:
     turtle.speed(100000000)
     start.forward(1)
     start.left(1)
     val+=1
 v2=0
 while v2<360:
     turtle.speed(100000000)
     start.forward(1)
     start.right(1)
     v2+=1
 y=1
 x=1
 turtle.goto(y,x)
 y+=1
 x+=1
turtle.done()