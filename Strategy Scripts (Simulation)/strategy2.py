import turtle
import math

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle object
t = turtle.Turtle()
t.speed(0)

r = 50                                     # Radius of circle -> Accuracy of stero-camera..


f1 = 1.9                                     # Radius factor for first polygon..
f2 = 3.65                                    # Radius factor for second polygon
f3 = 4.5                                     # Radius factor for final Range..
n = 20                                       # Number of sides of polygon..


# f1 = 1.85                                     # Radius factor for first polygon..
# f2 = 3.4                                    # Radius factor for second polygon
# f3 = 3.85                                     # Radius factor for final Range..
# n = 12                                       # Number of sides of polygon..


# Some function for drawing line/circle etc..

def turn(t):
    t.left(1)

def align_to_right(t):
   t.setheading(0)

def align(t, heading):
    t.setheading(heading)

def makecircle(t,r):
    
    current_pos = t.position()
    heading = t.heading()

    align_to_right(t)

    t.penup()
    t.goto(current_pos[0], current_pos[1] - r)

    t.fillcolor("blue")
    t.begin_fill()
    t.circle(r)
    t.end_fill()

    t.goto(current_pos)
    align(t,heading)
    t.pendown()


def draw_polygon(n, radius, t, circle = True):

    # Calculate the angle for each side of the polygon
    angle = 360 / n
    length = radius*math.sin(angle*math.pi/180)

    # Draw the polygon
    # t.circle(r)
    # t.setheading(15)

    t.setheading(0)
    for _ in range(n+1):
        if _ == 0 or _ == n:
            t.forward(length/2)
        else:
            t.forward(length)
        if circle: makecircle(t,r)
        t.right(angle)

t.forward(10)




makecircle(t,r)                                         # Scan at center..

current_pos = t.position()
t.penup()
t.goto(current_pos[0], current_pos[1] + f1*r)
t.pendown()
draw_polygon(n, f1*r, t)                                 # First Polygon...


t.penup()
current_pos = t.position()
t.goto(current_pos[0], current_pos[1] + (f2-f1)*r)
t.pendown()
draw_polygon(n, f2*r, t)                                 # Second Polygon...


t.penup()
current_pos = t.position()
t.goto(current_pos[0], current_pos[1] + (f3-f2)*r)
t.pendown()
draw_polygon(n, f3*r, t, circle = False)                   # Third Polygon...


current_pos = t.position()
print(current_pos)
print(((current_pos[0])**2 + (current_pos[1])**2)**(1/2))


# Keep the window open
screen.mainloop()