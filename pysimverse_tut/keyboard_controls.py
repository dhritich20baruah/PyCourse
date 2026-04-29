from pysimverse import Drone
import keyboard
import time

# Initialize drone
drone = Drone()
drone.connect()
drone.take_off()

SPEED = 50

try:
    while True:
        left_right = 0
        forward_backward = 0
        up_down = 0
        yaw = 0

        # LEFT / RIGHT
        if keyboard.is_pressed('left'):
            left_right = -SPEED
        elif keyboard.is_pressed('right'):
            left_right = SPEED

        # FORWARD / BACKWARD
        if keyboard.is_pressed('up'):
            forward_backward = SPEED
        elif keyboard.is_pressed('down'):
            forward_backward = -SPEED

        # UP / DOWN
        if keyboard.is_pressed('w'):
            up_down = SPEED
        elif keyboard.is_pressed('s'):
            up_down = -SPEED

        # YAW (ROTATION)
        if keyboard.is_pressed('a'):
            yaw = -SPEED
        elif keyboard.is_pressed('d'):
            yaw = SPEED

        # EXIT KEY (safe landing)
        if keyboard.is_pressed('q'):
            print("Landing...")
            break

        drone.send_rc_control(left_right, forward_backward, up_down, yaw)

        time.sleep(0.05)

finally:
    drone.land()
    time.sleep(1)