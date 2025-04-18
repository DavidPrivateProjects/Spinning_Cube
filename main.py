from math import cos, sin
import time
import keyboard

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
    for i in range(height):
        start = i * width
        line = ''.join(buffer[start:start + width])
        print(line)
    # Move cursor to top-left without clearing screen
    print('\x1b[H', end='')


# Helper: Python doesn't have a built-in float range
def frange(start, stop, step):
    while start < stop:
        yield start
        start += step


def handle_input():
    global vel_a, vel_b, vel_c

    delta = 0.0015  # Speed adjustment per keypress

    if keyboard.is_pressed('up'):
        vel_b -= delta
    if keyboard.is_pressed('down'):
        vel_b += delta
    if keyboard.is_pressed('left'):
        vel_a -= delta
    if keyboard.is_pressed('right'):
        vel_a += delta


if __name__ == "__main__":
    # Rotation angles
    a, b, c = 0, 0, 0
    # Angular velocities (momentum)
    vel_a, vel_b, vel_c = 0.1, 0.1, 0.1
    
    # Constants
    cube_width = 10
    width, height = 160, 44
    background_ascii_code = ' '
    inc_speed = 1
    dist_from_cam = 100
    k1 = 40
    # Inertia (friction factor)
    inertia = 0.98



    time.sleep(5)
    while True:
        buffer = [background_ascii_code] * (width * height)
        zbuffer = [0] * (width * height)


        # Input handling
        handle_input()

        for cube_x in frange(-cube_width, cube_width, inc_speed):
            for cube_y in frange(-cube_width, cube_width, inc_speed):
                calc_surface(cube_x, cube_y, -cube_width, '@')
                calc_surface(cube_width, cube_y, cube_x, '$')
                calc_surface(-cube_width, cube_y, -cube_x, '~')
                calc_surface(-cube_x, cube_y, cube_width, '#')
                calc_surface(cube_x, -cube_width, -cube_y, ';')
                calc_surface(cube_x, cube_width, cube_y, '+')
        
        render_frame()

        # Update rotation angles with momentum
        a += vel_a
        b += vel_b
        c += vel_c

        # Apply inertia
        vel_a *= inertia
        vel_b *= inertia
        vel_c *= inertia

        time.sleep(0.003)
        

