""" This is your starter code for the Asteroid Kaboom assignment.

Bahar Nikfalazar, 400673513,
in this program we are going to create a game.......
DO NOT FORGET THIS

You should rename this file and replace this docstring with your own,
as per the documentation standards.

To use this template, make sure that both this file and pixels.py are in the
same folder. From Pyzo, choose Run File as Script.

This template allows you to use a special check_pixel_color function.

For example, check_pixel_color(0, 0, "green") will return 1 if the pixel
at location (0,0) is "green", or 0 if it is not. When you are assigning
points for shots in the assignment, you can multiply the return value by
the number of points for hitting that color.

Sam Scott, McMaster, 2025"""

# Import the turtle module
import turtle
from pixels import check_pixel_color

import random # this used for the random locations for the star and astroids

# Constants (you can change these)
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 450
WINDOW_TITLE = "My First Turtle Program"

# Set up the screen object
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen = turtle.Screen()
screen.title(WINDOW_TITLE)
screen.bgcolor("black")# i wanted to make the background color black so i added this here
# Create the turtle object
t = turtle.Turtle()

## Start of your code

# example of how to use check_pixel_color
print( check_pixel_color(100, 0, "white") ) # returns 1
print( check_pixel_color(0, 0, "white") )   # returns 0



##Task 1, star

#this function helps us to draw several stars with a random locations, stars are centered at x y, and i used for loop, random library used here for the location, size and the color
def star(x,y, size = 20, color = "white"):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(color)

#with the help of this for loop, we draw one star and we are also giving the information on how to draw a 5 sides star so later in the function it will use it to draw a single star and put it in the random locations
    for i in range(5):
        t.forward(size)
        t.right(144)
    t.penup()

screen.tracer(0) #this turns off the animation for faster drawing


#these code lines here are helping to get a random stuff like number for the size and by having the random it can help us to choose any random things from the color array from the library

for _ in range(50): #going to modify 50 stars
    rand_x = random.randint(-SCREEN_WIDTH// 2, SCREEN_WIDTH //2)
    rand_y = random.randint(-SCREEN_HEIGHT//2, SCREEN_HEIGHT //2)
    rand_size = random.randint(10,30)
    rand_color = random.choice(["white", "yellow", "lightblue", "pink"])#making stars look more nice :)

#setting the star
    star(rand_x, rand_y, rand_size, rand_color)

screen.update()
##End of Task 1


##Task 2, Polygon

#this function helps us to draw several polygon with a random locations, random library used here to generate the location and the size of the polygon
def asteroid(x, y, size =40, sides =6, color = "pink", angle = 0):
    t.penup()
    t.goto(x,y)
    t.setheading(angle) # for the rotation of the asteroid
    t.pendown()
    t.color(color)
    t.begin_fill()


# this for loop is for one polygon(asteroid), later in the code we will use this to draw multiple of them
    for _ in range(sides):
        t.forward(size)
        t.right(360 / sides)
    t.end_fill()
    t.penup()

#draw random asteroids
for _ in range(15):
    rand_x = random.randint(-SCREEN_WIDTH //2 , SCREEN_WIDTH //2)
    rand_y = random.randint(-SCREEN_HEIGHT // 2, SCREEN_HEIGHT //2)
    rand_size = random.randint(20,60)
    rand_angle = random.randint(0, 360)
    rand_color = random.choice(["pink", "green"])
    rand_sides = random.choice([5,6,7,8])

    asteroid(rand_x, rand_y, size=rand_size, sides = rand_sides, color = rand_color, angle = rand_angle)

# we want to make sure that always one asteroid is places in the 0,0 location, also for myself to understand better i set the color to the dark red to be different with others
asteroid(0,0, size = 50, sides = 6, color = "darkred", angle = random.randint(0,360))

screen.update()
##End of Task 2


##Task 3 - 6 , Polygon Shooting , Explosions, Scoring,

#taking these variables , user input and the assigned score variable
num_shots = int(screen.numinput("Kaboom Attack!", "How mant shots would you like to take?", minval = 1, maxval = 20))

total_score = 0


#this function is going to draw the shooting design, continiuing by matching the position of the shots given from the user, based on the user shots it has a for loop to ask for the xy of each shot from the user, the shots validity will check from matching it the position has a color the same as the polygons
def explosion(x,y, points):

    #this part is for one simple explosion
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("orange")

    #draw the shoots
    for angle in range(0,360, 45):
        t.setheading(angle)
        t.forward(20)
        t.backward(40)
        t.forward(20)


    #showing the score text(desing of the score when it is going to display for each shoot)
    t.penup()
    t.goto(x, y - 40)
    t.color("white")
    t.write(f"+{points} points", align= "center", font=("Arial", 12 , "bold"))


    #loop for shots
for i in range(num_shots):
    shot_x = int(screen.numinput("Asteroid ATTACK!", f"Enter X position for the shot #{i+1} (-450, 450):", minval=-450, maxval = 450))
    shot_y = int(screen.numinput("Asteroid ATTACK!!", f"Enter the Y position for the shot #{i+1} (-225, 225):", minval = -225, maxval = 225))
    #this part is to check the shot hits the polygon or not based on matching the color
    points = 10 * (
        check_pixel_color(shot_x, shot_y, "pink")
        or check_pixel_color(shot_x, shot_y, "green")
        or check_pixel_color(shot_x, shot_y, "darkred"))

    total_score += points
    explosion(shot_x, shot_y, points)


#displaying all the shootings and final result
t.goto(0, SCREEN_HEIGHT//2 - 40)
t.color("yellow")
t.write(f"Final Score: {total_score}", align = "center", font= ("Arial" , 20 , "bold"))




## End of your code

# Make a clean exit
screen.exitonclick()
