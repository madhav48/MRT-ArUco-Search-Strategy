import turtle

# Create a turtle object
t = turtle.Turtle()
t.speed(0)


r = 50                                   # Radius of circle -> Accuracy of stero-camera..

n = 23                                    # Max edge iteration
x = 45                                  # Starting edge length
f = 0.25                                 # Fraction by which edge length should be increased..
sections = 0.75                           # Number of sections for even square index..
sections_inc = 1/4


i = 1                                     # Edge counter
side = 1                                  # Sqaure sides counter
flag = 1                                  # Odd/even..


inital_pos = t.position()             # Record inital position
move_sum = 0                          # Record Move distance...

# Some function for drawing line/circle etc..

def move(t, x):
    global move_sum
    move_sum += x
    t.forward(x)

def turn(t):
    t.left(90)

def align_to_right(t):
    while t.heading() != 0.0: 
        turn(t)
    return

def align(t, heading):
    while t.heading() != heading:
        turn(t)

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

makecircle(t,r)
while i <= n:

    if flag:                        # Odd index..
        move(t,(x + x*i*f))
        makecircle(t,r)
    else:                             # Even index
        points = 2*int(sections) - 1
        for j in range(points+1):
            move(t,(x + x*i*f)/(points+1))
            if not(j == points):
                makecircle(t,r)
            
    turn(t) 

    side += 1
    if side == 4:               # On completing a sqaure..
        side = 0
        flag = (flag == 0)
        sections += sections_inc
    i += 1

final_pos = t.position()               # Record final position..
range_traversed = ((final_pos[0]-inital_pos[0])**2 + (final_pos[1]-inital_pos[1])**2)**(1/2)
print(range_traversed)                 # Range covered..
print(move_sum)

# Keep the window open
turtle.done()