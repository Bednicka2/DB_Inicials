import turtle

s = turtle.Screen()
s.setup(width=500, height=600)
s.bgcolor('black')
t1, t2 = turtle.Turtle(), turtle.Turtle()

# t1 set-up
t1.speed(0)
t1.hideturtle()
t1.pensize(1)
colors2 = ('goldenrod1', 'goldenrod2', 'goldenrod', 'goldenrod3', 'goldenrod4')

# t2 set-up
t2.speed(0)
t2.hideturtle()
t2.pensize(1)
colors1 = ('blue', 'blue2', 'medium blue', 'dark blue', 'midnight blue')

# starting position t1
t1.goto(-100, -50)
t1.left(90)
t1.pendown()

# starting position t2
t2.goto(-30, -160)
t2.left(90)
t2.pendown()

# drawing
for i in range(30):
    if i % 6 == 0:
        t1.pencolor(colors1[i % 5])
        t2.pencolor(colors2[i % 5])
    t1.forward(200)
    t2.forward(200)
    t1.right(90)
    t2.right(90)
    t1.circle(-100, 90)
    t2.circle(-50, 60)
    t2.circle(-30, 60)
    t2.circle(-50, 60)
    t2.right(-180)
    t1.circle(-100, 90)
    t2.circle(-80, 60)
    t2.circle(-40, 60)
    t2.circle(-80, 60)
    t1.goto(-100 + i*2, -50)
    t2.goto(-30 + i*2, -160)
    t1.right(90)
    t2.right(90)

# stay open
s.exitonclick()
