from turtle import *
def draw_square(i, color):
    pencolor(color)
    for i in range(4):
        forward(i)
        right(90)
    mainloop()

draw_square(100, "red")
