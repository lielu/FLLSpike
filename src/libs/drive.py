<<<<<<< HEAD
def straight(motor, speed, distance=None, degrees=None, seconds=None):
    """
    Control a drive motor for FLL Spike.
    
    Args:
        motor: The motor object to control.
        speed (int): The speed of the motor (-100 to 100).
        distance (float, optional): The distance to travel in centimeters.
        degrees (int, optional): The number of degrees to rotate the motor.
        seconds (float, optional): The number of seconds to run the motor.
    """
    if distance is not None:
        # Assuming a standard wheel diameter of 5.6 cm for LEGO wheels
        # Circumference = pi * diameter
        wheel_circumference = 3.14159 * 5.6
        # Calculate degrees to rotate based on distance
        degrees_to_rotate = (distance / wheel_circumference) * 360
        motor.run_for_degrees(int(degrees_to_rotate), speed)
    elif degrees is not None:
        motor.run_for_degrees(degrees, speed)
    elif seconds is not None:
        motor.run_for_seconds(seconds, speed)
    else:
        motor.start(speed)

    motor.wait_until_not_moving()


=======
from hub import port, motion_sensor
import motor #imports a ability to control a single motor
import motor_pair #imports a pair of motors moving like one

distanceInDegrees = 0
current_yaw_position = 0

def init():
    motor_pair.pair(motor_pair.PAIR_1, port.F, port.E) #Motor pair called motor_pair.PAIR_1, left motor: port A, right motor: port B
    motion_sensor.reset_yaw(0) #Makes the robot think its facing forward.

def forward(distance, speed): #FUNCTION
    init()
    global current_yaw_position, distanceInDegrees
    distanceInDegrees = distance / 28 * 360
    current_yaw_position = motion_sensor.tilt_angles()[0]
    motor.reset_relative_position(port.E, 0) 
    while motor.relative_position(port.E) < distanceInDegrees:
        motor_pair.move_for_degrees(motor_pair.PAIR_1, 5, current_yaw_position * -3, velocity=int(round(speed/100.0*660.0)))
        current_yaw_position = motion_sensor.tilt_angles()[0]
    motor_pair.stop(motor_pair.PAIR_1)

def backward(distance, speed): #FUNCTION
    motion_sensor.reset_yaw(0)
    motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)
    global current_yaw_position, distanceInDegrees
    distanceInDegrees = distance / 28 * 360
    current_yaw_position = motion_sensor.tilt_angles()[0]
    motor.reset_relative_position(port.E, 0)
    while motor.relative_position(port.E) < distanceInDegrees:
        motor_pair.move_for_degrees(motor_pair.PAIR_1, 5, current_yaw_position * -3, velocity=int(round(speed/100.0*660.0)))
        current_yaw_position = motion_sensor.tilt_angles()[0]
    motor_pair.stop(motor_pair.PAIR_1)

def turnRight(degrees):
    init()
    current_yaw_position = motion_sensor.tilt_angles()[0]
    while current_yaw_position < degrees:
        motor_pair.move_for_degrees(motor_pair.PAIR_1, 1, 100)
        current_yaw_position = motion_sensor.tilt_angles()[0]

def turnLeft(degrees):
    init()
    current_yaw_position = motion_sensor.tilt_angles()[0]
    while current_yaw_position > degrees:
        motor_pair.move_for_degrees(motor_pair.PAIR_1, -1, 100)
        current_yaw_position = motion_sensor.tilt_angles()[0]

turnRight(90)
>>>>>>> 6826e273ce5fd4df1d34f75a58fdc819ffbdcc4b
