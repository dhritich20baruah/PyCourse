from pysimverse import Drone
import time

# Initialization
drone = Drone()
drone.connect()
drone.take_off()

drone.set_speed(50)
drone.move_left(20)
time.sleep(2)
# drone.rotate(45)
drone.move_forward(50)
time.sleep(2)
# drone.move_right(30)
# time.sleep(2)
# drone.rotate(-90)
# drone.move_backward(50)
# time.sleep(2)

drone.land()
time.sleep(1)