from math import cos, sin
import time
import keyboard


class Cube:
    def __init__(self, width=160, height=44, cube_size=10):
        self.width = width
        self.height = height
        self.cube_size = cube_size
        self.background = ' '
        self.buffer = [' '] * (self.width * self.height)
        self.zbuffer = [0] * (self.width * self.height)
        self.k1 = 40  # Projection constant
        self.dist_from_cam = 100
        self.inc = 1  # Increment step for plotting cube
        self.inertia = 0.98

        # Rotation angles
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0

        # Angular velocities (momentum)
        self.vel_a = 0.1
        self.vel_b = 0.1
        self.vel_c = 0.1

    def get_x(self, i, j, k):
        return (j * sin(self.a) * sin(self.b) * cos(self.c)
                - k * cos(self.a) * sin(self.b) * cos(self.c)
                + j * cos(self.a) * sin(self.c)
                + k * sin(self.a) * sin(self.c)
                + i * cos(self.b) * cos(self.c))

    def get_y(self, i, j, k):
        return (j * cos(self.a) * cos(self.c)
                + k * sin(self.a) * cos(self.c)
                - j * sin(self.a) * sin(self.b) * sin(self.c)
                + k * cos(self.a) * sin(self.b) * sin(self.c)
                - i * cos(self.b) * sin(self.c))

    def get_z(self, i, j, k):
        return (k * cos(self.a) * cos(self.b)
                - j * sin(self.a) * cos(self.b)
                + i * sin(self.b))

    def calc_surface(self, i, j, k, char):
        """Project a 3D point (i, j, k) into 2D and place it in the buffer if visible"""
        x = self.get_x(i, j, k)
        y = self.get_y(i, j, k)
        z = self.get_z(i, j, k) + self.dist_from_cam

        ooz = 1 / z
        xp = int(self.width / 2 + self.k1 * ooz * x * 2)
        yp = int(self.height / 2 + self.k1 * ooz * y)

        idx = xp + yp * self.width
        if 0 <= idx < self.width * self.height:
            if ooz > self.zbuffer[idx]:
                self.zbuffer[idx] = ooz
                self.buffer[idx] = char

    def frange(self, start, stop, step):
        """Like range(), but for floats"""
        while start < stop:
            yield start
            start += step

    def render_key_status_to_buffer(self):
        """Render arrow key status into the buffer (bottom-left corner)"""
        status_lines = [
            "Controls:",
            f"↑ UP:    [{'X' if keyboard.is_pressed('up') else ' '}]",
            f"↓ DOWN:  [{'X' if keyboard.is_pressed('down') else ' '}]",
            f"← LEFT:  [{'X' if keyboard.is_pressed('left') else ' '}]",
            f"→ RIGHT: [{'X' if keyboard.is_pressed('right') else ' '}]",
        ]

        base_y = self.height - len(status_lines) - 1  # Render from bottom up
        base_x = 2  # Small indent from left

        for i, line in enumerate(status_lines):
            for j, char in enumerate(line):
                x = base_x + j
                y = base_y + i
                if 0 <= x < self.width and 0 <= y < self.height:
                    self.buffer[y * self.width + x] = char


    def render_frame(self):
        """Draw buffer to terminal"""
        print('\x1b[H', end='')  # Move cursor to top-left
        for i in range(self.height):
            start = i * self.width
            line = ''.join(self.buffer[start:start + self.width])
            print(line)


    def handle_input(self):
        """Check for keyboard input and apply rotation momentum"""
        delta = 0.0015
        if keyboard.is_pressed('up'):
            self.vel_b -= delta
        if keyboard.is_pressed('down'):
            self.vel_b += delta
        if keyboard.is_pressed('left'):
            self.vel_a -= delta
        if keyboard.is_pressed('right'):
            self.vel_a += delta


    def update(self):
        """Clear buffers, handle input, draw cube surfaces, update physics"""
        self.buffer = [self.background] * (self.width * self.height)
        self.zbuffer = [0] * (self.width * self.height)

        self.handle_input()

        # Draw all cube faces
        for x in self.frange(-self.cube_size, self.cube_size, self.inc):
            for y in self.frange(-self.cube_size, self.cube_size, self.inc):
                self.calc_surface(x, y, -self.cube_size, '@')
                self.calc_surface(self.cube_size, y, x, '$')
                self.calc_surface(-self.cube_size, y, -x, '~')
                self.calc_surface(-x, y, self.cube_size, '#')
                self.calc_surface(x, -self.cube_size, -y, ';')
                self.calc_surface(x, self.cube_size, y, '+')

        self.render_key_status_to_buffer()
        self.render_frame()

        # Apply angular velocity
        self.a += self.vel_a
        self.b += self.vel_b
        self.c += self.vel_c

        # Apply damping/inertia
        self.vel_a *= self.inertia
        self.vel_b *= self.inertia
        self.vel_c *= self.inertia

    def run(self):
        """Main loop"""
        #print('\x1b[2J')  # Clear screen
        time.sleep(5)
        while True:
            self.update()
            time.sleep(0.003)


if __name__ == "__main__":
    cube = Cube()
    cube.run()

        

