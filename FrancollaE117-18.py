#Import turtle library for drawing functions and sprites
import turtle as trtl

#Set my_Turtles as an empty lies
my_turtles = []

#Use different shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic" ]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple",  "gold" ]

#For loop setting t to the turtle object and adding it to the my_turtles list
for s in turtle_shapes:
    #Create turtle object
    t = trtl.Turtle(shape=s)
    t.penup()
    pensize = 1
    t.pensize(pensize)

    #Color the turtle object
    new_color = turtle_colors.pop()
    t.pencolor(new_color)
    t.fillcolor(new_color)

    #Add new turtle to my_turtles list
    my_turtles.append(t)

#Set starting positions of turtles  
startx = 0
starty = 0
heading = 45
heading_change = 1.03
intial_forward_motion = 15

#For loops moving turtles to designnated spots
for t in my_turtles:
    #Set initial position
    t.goto(startx, starty)
    t.pensize(pensize)
    t.pendown()

    #Move turtle with correct length and angle
    t.right(heading)
    t.forward(intial_forward_motion)
    
    #Change starting position and heading for next turtle so it starts where the last one left off
    startx = t.xcor()
    starty = t.ycor()
    heading = heading * heading_change + 45
    intial_forward_motion = intial_forward_motion + 10
    pensize = pensize + 1

#Display screen and keep it persistent
wn = trtl.Screen()
wn.mainloop()