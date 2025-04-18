# ASCII Spinning Cube with Keyboard Interactivity

A real-time 3D ASCII cube rendered in the terminal using Python. This project features dynamic cube rotation with keyboard-controlled momentum and inertia for a smooth, physics-inspired experience.

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
Each face of the cube is rendered by projecting 3D points into 2D space using trigonometric transformations.

A z-buffer is used to simulate depth, ensuring only the nearest surfaces are drawn.

Momentum is simulated using angular velocities that persist and decay over time.

Known Limitations
Requires a terminal that supports ANSI escape codes (for cursor positioning)

Keyboard input may require administrator privileges, depending on the OS

Resizing the terminal during execution may cause rendering glitches

## License
This project is licensed under the MIT License.
