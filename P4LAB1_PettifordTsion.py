from turtle import *
#Tsion Pettiford
#10/31/2023
#using for loops to draw shapes 

#Create the turtle object
timmy = Turtle()
timmy.color("light blue")

#Draw the square
#Set the pen down
timmy.pendown()
timmy.forward(50)         #move forward 50 spaces
timmy.left(90)            #turn left 90 degrees
timmy.forward(50)   
timmy.left(90)  
timmy.forward(50)   #from all of these lines of code
timmy.left(90)
timmy.forward (50)
timmy.penup()
timmy.forward(10)
timmy.pendown()

#make the for loop
for n in range(4):
    timmy.forward(50)        #to these few lines of code
    timmy.left(90)


