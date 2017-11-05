import turtle
t=turtle.Turtle()

def square(length, angle):
    for i in range(3):
        t.forward(length)
        t.left(angle)

    t.forward(length)

t.speed(0)


for i in range(1000):
    for b in range(15):
        t.color("Blue")
        square(100, 90)
        t.left(97)
    for r in range(15):    
        t.color("Red")
        square(100, 90)
        t.left(97)
    for y in range(15):
        t.color("Yellow")
        square(100, 90)
        t.left(97)
    for g in range(15):
        t.color("Green")
        square(100, 90)
        t.left(97)



