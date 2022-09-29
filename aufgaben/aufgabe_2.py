from turtle import forward, right, left, done, penup, pendown
from time import sleep

# 2a)
def draw_equilateral_triangle(side_length):
    for i in range(3):
        forward(side_length)
        left(120)

triangle_side_length = 100

draw_equilateral_triangle(side_length=triangle_side_length)

# 2b)

penup()
left(60)
forward(2*triangle_side_length)
left(120)
pendown()
draw_equilateral_triangle(side_length=triangle_side_length)
done()  # prevents turtle drawing window from closing immediately
