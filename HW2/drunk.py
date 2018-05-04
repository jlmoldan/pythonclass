# Jason Moldan
# HW2
# drunk.py

import math, random, turtle
numSteps=input("Enter number of steps: ")
numSteps=int(numSteps)

wn = turtle.Screen()             # Set up the window and its attributes
turtle.Turtle
#turtle.speed(0)


for steps in range(numSteps):
   x=random.randrange(0,360)
   turtle.setheading(x)
   turtle.forward(5)

# turtle.home()
#print (turtle.position())
pos = turtle.position()
#print (pos)
print (pos)
#turtle.distance(turtle)
#turtlex=turtle.xcor
#turtley=turtle.ycor

turtle.distance(0,0, )

wn.exitonclick()
