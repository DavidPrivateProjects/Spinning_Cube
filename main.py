import math
from math import cos as cos
from math import sin as sin
import os

cube_width = 10
width, height = 160, 44
zbuffer = [None] * 160 * 44
buffer = [None] * 160 * 44
background_ascii_code = ' '
inc_speed = 1
dist_from_cam = 60
k1 = 40
idx = None


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


def calc_surface(i, j, k, char):
    x = get_x(i, j, k)
    y = get_y(i, j, k)
    z = get_z(i, j, k) + dist_from_cam

    ooz = 1/z

    xp = width / 2 + k1 * ooz * x * 2
    yp = height / 2 + k1 * ooz * y

    idx = xp + yp * width
    if idx >= 0 and idx < width * height:
        if ooz > zbuffer[idx]:
            buffer[idx] = char


def main():
    print()
    #os.system("cls") # delete the current screen in windows
    while True:
        background = [background_ascii_code * width * height]
        for x in range(-cube_width, cube_width, inc_speed):
            for y in range(-cube_width, cube_width, inc_speed):
                for z in range(-cube_width, cube_width, inc_speed):
                    calc_surface(x, y, -cube_width, '#')
        
        for k in range(0, width * height):
            putchar(k % width ? buffer[k] : 10)

        a += 0.005
        b += 0.005



main()