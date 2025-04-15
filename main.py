import math
from math import cos as cos
from math import sin as sin

cube_width = 10
width, height = 160, 44
zbuffer = 160 * 44
buffer = 160 * 44
background_ascii_code = ' '
inc_speed = 1

def get_x(i, j, k):
    return (  j * sin(a) * sin(b) * cos(c) 
            - k * cos(a) * sin(b) * cos(c)
            + j * cos(a) * sin(c) 
            + k * sin(a) * sin(c)
            + i * cos(b) * cos(c))

def get_y(i, j, k):
    return (  j * cos(a) * cos(c) 
            + k * sin(a) * cos(c)
            - j * sin(a) * sin(b) * sin(c) 
            + k * cos(a) * sin(b) * sin(c)
            - i * cos(b) * sin(c))

def get_z(i, j, k):
    return (  k * cos(a) * cos(b) 
            - j * sin(a) * cos(b)
            + i * sin(b))


def main():
    while True:
        background = [background_ascii_code * width * height]
        for x in range(-cube_width, cube_width, inc_speed):
            for y in range(-cube_width, cube_width, inc_speed):
                for z in range(-cube_width, cube_width, inc_speed):

main()