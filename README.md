# Automating Two Cars Android Game

This project automates the **Two Cars** Android game, where two cars navigate four lanes to collect circles and avoid squares. The game is played using **OpenCV** for real-time object detection and **scrcpy** for controlling the mobile device. The cars alternate between two lanes: 
- Car 1 switches between lane 1 and lane 2
- Car 2 switches between lane 3 and lane 4

The objective of the game is to collect **circles** and avoid **squares** on all lanes.

## Technologies Used

- **Python**: The programming language used for the automation script.
- **OpenCV**: A powerful computer vision library used for detecting and recognizing shapes (circles and squares) on the game screen.
- **scrcpy**: A tool that allows you to mirror and control Android devices via USB or TCP connection. Used for sending controls to the game.

## How the Automation Works

The automation involves detecting the shapes on the lanes in real-time and making decisions about which car needs to switch lanes to either collect a circle or avoid a square.

### Workflow

1. **Screen Mirroring with scrcpy**:
   - The game screen is mirrored on the computer using **scrcpy**.
   - This allows the screen to be captured and processed for detecting objects (circles and squares) on the lanes.

2. **Frame Capture using OpenCV**:
   - **OpenCV** captures each frame from the mirrored screen in real-time.
   - The frame is converted to grayscale for easier shape detection.

3. **Shape Detection using Contours**:
   - **Contour detection** in OpenCV is used to detect shapes on the lanes.
   - Circles and squares are identified by their contours:
     - **Circles** are recognized by checking the roundness of the shape.
     - **Squares** are recognized by detecting the four edges and right angles.

4. **Lane Assignment**:
   - Each detected object (circle or square) is assigned to one of the four lanes.
   - The automation decides which car (Car 1 or Car 2) needs to switch lanes based on the location of the detected objects.

5. **Car Movement**:
   - Based on the positions of circles and squares, the script sends commands via **scrcpy** to control the cars:
     - Switch lanes to collect **circles**.
     - Avoid **squares** by switching lanes.

### Decision Logic

- If a **circle** is detected in the current lane, the car continues in that lane.
- If a **square** is detected, the car switches to the alternate lane to avoid it.
- The system constantly monitors all four lanes to ensure both cars navigate correctly.

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python** 3.x
- **OpenCV**: Install using `pip`:
    ```bash
    pip install opencv-python
    ```
- **scrcpy**: Follow the [official installation guide](https://github.com/Genymobile/scrcpy) to set up scrcpy for Android screen mirroring.

Make sure your Android device is connected via USB and **Developer Options** are enabled for scrcpy to work.

## Usage

1. Clone the repository and navigate to the project directory.
2. Launch **scrcpy** to mirror your Android device:
   ```bash
   scrcpy
