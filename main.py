import math
from math import cos as cos
from math import sin as sin

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