from math import cos as cos
from math import sin as sin
import os
import time
import sys


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


def calc_surface(i, j, k, chr):
    global x, y, z, ooz, xp, yp, idx
    x = get_x(i, j, k)
    y = get_y(i, j, k)
    z = get_z(i, j, k) + dist_from_cam

    ooz = 1/z

    xp = int(width / 2 + k1 * ooz * x * 2)
    yp = int(height / 2 + k1 * ooz * y)

    idx = xp + yp * width
    if 0 <= idx < width * height:
        if ooz > zbuffer[idx]:
            zbuffer[idx] = ooz
            buffer[idx] = chr

def render_frame():
    print('\x1b[H', end='')  # Move cursor to top-left without clearing screen
    """for i in range(height):
        start = i * width
        line = ''.join(buffer[start:start + width])
        print(line)"""
    for k in range(width * height):
        print(buffer[k], end='' if k % width else '\n')


# Helper: Python doesn't have a built-in float range
def frange(start, stop, step):
    while start < stop:
        yield start
        start += step


if __name__ == "__main__":
    # Rotation angles
    a, b, c = 0, 0, 0
    
    # Constants
    cube_width = 10
    width, height = 160, 44
    background_ascii_code = '.'
    inc_speed = 1
    dist_from_cam = 100
    k1 = 40
    print("\x1b[2J") 

    #os.system("cls") # delete the current screen in windows
    while True:
        buffer = [background_ascii_code] * (width * height)
        zbuffer = [0] * (width * height)
        for cube_x in frange(-cube_width, cube_width, inc_speed):
            for cube_y in frange(-cube_width, cube_width, inc_speed):
                calc_surface(cube_x, cube_y, -cube_width, '@')
                calc_surface(cube_width, cube_y, cube_x, '$')
                calc_surface(-cube_width, cube_y, -cube_x, '~')
                calc_surface(-cube_x, cube_y, cube_width, '#')
                calc_surface(cube_x, -cube_width, -cube_y, ';')
                calc_surface(cube_x, cube_width, cube_y, '+')
        
        
        render_frame()
        a += 0.005
        b += 0.005
        c += 0.01
        time.sleep(0.003)
        

