from pysimverse import Drone
import time

# Initialization
drone = Drone()
drone.connect()
drone.take_off()

drone.set_speed(75)
drone.rotate(47)
drone.move_forward(350)
drone.rotate(-47)

drone.land()
time.sleep(1)