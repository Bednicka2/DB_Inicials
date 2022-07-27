import turtle
import tkinter
from PIL import Image
import os
import time


### This will create .eps and png files ####
def png(i):
    # keeping eps file name as image
    eps_file = str(i)+"temp.eps"

    # generating eps file
    ts = turtle.getscreen()
    turtle.hideturtle()
    turtle.penup()
    ts.getcanvas().postscript(file=eps_file)

    # get png using ghost script"
    filename = eps_file.replace('.eps', '.png')
    os.popen(f"gswin64c -dSAFER -dBATCH -dNOPAUSE -r300 -sDEVICE=pngalpha -dTextAlphaBits=4 -dGraphicsAlphaBits=4 "
             f"-sOutputFile={filename} -dEPSCrop {i}temp.eps")

    # Merge transparent png on top of given background png
    time.sleep(2)


def main():
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
    t1.penup()
    t1.goto(-100, -50)
    t1.left(90)
    t1.pendown()

    # starting position t2
    t2.penup()
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
        png(i)

    # stay open
    print("Exit on click")
    s.exitonclick()


if __name__ == "__main__":
    main()  
    
