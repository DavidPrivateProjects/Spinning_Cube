# ASCII Spinning Cube with Keyboard Interactivity

A real-time 3D ASCII cube rendered in the terminal using Python. This project features dynamic cube rotation with keyboard-controlled momentum and inertia for a smooth, physics-inspired experience.



https://github.com/user-attachments/assets/1ac721a4-6463-4527-b8f0-38f0a26156ea



## Features

- Rotating 3D cube rendered using ASCII characters
- Arrow key input for interactive rotation:
  - Up / Down — Rotate along X-axis
  - Left / Right — Rotate along Y-axis
- Momentum and inertia: cube keeps spinning even after releasing keys
- Real-time rendering in terminal using projection and z-buffering
- On-screen display showing current control input status

## Requirements

- Python 3.7+
- `keyboard` library (for arrow key detection)

Install dependencies using:

pip install keyboard

## Usage
bash
Copy
Edit
python cube.py
Once launched, the cube will start spinning automatically. Use the arrow keys to influence its rotation:

Hold keys to add spin in a direction

Release keys to let inertia take over

Note: On some systems, running the script might require elevated permissions for keyboard access. If you encounter permission errors, try:

bash
Copy
Edit
sudo python cube.py
Customization
You can adjust cube parameters in the Cube class constructor:

python
Copy
Edit
cube = Cube(width=160, height=44, cube_size=10)
width / height: Terminal dimensions (in characters)

cube_size: Size of the cube

inertia: Controls damping (closer to 1 means more persistent spin)

## How It Works
The spinning cube is a terminal-based 3D animation using ASCII characters. It relies on 3D rotation, projection, and depth buffering.

1. 3D Rotation
The cube exists in a 3D coordinate system (X, Y, Z).

Each cube point (i, j, k) is rotated using three angles:

A (rotation around X-axis)

B (rotation around Y-axis)

C (rotation around Z-axis)

Rotation is applied using rotation matrices:

Each rotation matrix transforms the point around a specific axis.

The final position is calculated by multiplying the point by the X, Y, and Z rotation matrices in sequence.

2. Projection to 2D
The 3D coordinates are projected onto a 2D screen using perspective projection:
​
<img width="74" alt="image" src="https://github.com/user-attachments/assets/5cf23794-f561-417c-8d00-4a672e892d73" />


K1 is a constant representing camera distance from screen.

The result is then offset to center the image in the terminal window.

3. Z-Buffering (Depth Perception)
Without depth handling, farther points may render over closer ones.

A z-buffer is used to store the depth (z-value) of each pixel.

Only points closer to the camera update the screen, creating proper depth illusion.

## License
This project is licensed under the MIT License.
