from turtle import *

def draw_star(x,y,length):
    penup()
    goto(x,y)
    pendown()
    i = 0
    while i <= 5:

        forward(length)
        right(144)
        i+=1

    mainloop()

# draw_star(200,110,100)