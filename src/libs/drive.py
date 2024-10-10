from hub import port, motion_sensor
import motor #imports a ability to control a single motor
import motor_pair #imports a pair of motors moving like one

distanceInDegrees = 0
current_yaw_position = 0

def init():
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C) #Motor pair called motor_pair.PAIR_1, left motor: port A, right motor: port B
    motion_sensor.reset_yaw(0) #Makes the robot think its facing forward.

def forward(distance, speed): #FUNCTION
    init()
    global current_yaw_position, distanceInDegrees
    distanceInDegrees = distance / 17.5 * 360
    current_yaw_position = motion_sensor.tilt_angles()[0]
    motor.reset_relative_position(port.C, 0) 
    while motor.relative_position(port.C) < distanceInDegrees:
        motor_pair.move_for_degrees(motor_pair.PAIR_1, 5, current_yaw_position * -3, velocity=int(round(speed/100.0*660.0)))
        if ValueError:
            motor_pair.move_for_degrees(motor_pair.PAIR_1, 5, current_yaw_position * -1, velocity=int(round(speed/100.0*660.0)))
        current_yaw_position = motion_sensor.tilt_angles()[0]
    motor_pair.stop(motor_pair.PAIR_1)

def backward(distance, speed): #FUNCTION
    motion_sensor.reset_yaw(0)
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)
    global current_yaw_position, distanceInDegrees
    distanceInDegrees = distance / 17.5 * 360
    current_yaw_position = motion_sensor.tilt_angles()[0]
    motor.reset_relative_position(port.C, 0)
    while motor.relative_position(port.C) < distanceInDegrees:
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

forward(20, 50)