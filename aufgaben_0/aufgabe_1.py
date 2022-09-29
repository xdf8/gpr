from math import pi
from turtle import forward, right, left, done


def right_half_circle(size):
    for i in range(18):
        forward(size * pi / 36)
        right(10)


left(90)
forward(250)
right(90)
right_half_circle(size=100)
forward(100*pi/36)
left(180)
right_half_circle(size=150)
forward(150*pi/36)
left(180)
done()  # prevents turtle drawing window from closing immediately
