from hub import port, motion_sensor
import motor #imports a ability to control a single motor
import motor_pair #imports a pair of motors moving like one
import runloop

distanceInDegrees = 0
current_yaw_position = 0

async def init_drive():
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C) #Motor pair called motor_pair.PAIR_1, left motor: port D, right motor: port C
    motion_sensor.reset_yaw(0) #Makes the robot think its facing forward.
    runloop.until(motion_sensor.stable)

async def forward(distance, speed): #FUNCTION
    await init_drive()
    global current_yaw_position, distanceInDegrees
    distanceInDegrees = distance / 17.5 * 360
    motor.reset_relative_position(port.C, 0) 
    while motor.relative_position(port.C) < distanceInDegrees:
        current_yaw_position = motion_sensor.tilt_angles()[0]
        adjusted = int(round(0.3 * current_yaw_position)) # tilt_angles are in decidegrees (degrees * 10)
        try:
            motor_pair.move_for_degrees(motor_pair.PAIR_1, 10, adjusted, velocity=int(round(speed/100.0*660.0)))
        except(ValueError):
            print('value error: ', adjusted)
            motor_pair.move_for_degrees(motor_pair.PAIR_1, 10, int(round(adjusted / 3)), velocity=int(round(speed/100.0*660.0)))
    motor_pair.stop(motor_pair.PAIR_1)

async def backward(distance, speed): #FUNCTION
    await init_drive()
    global current_yaw_position, distanceInDegrees
    distanceInDegrees = distance / 17.5 * 360
    motor.reset_relative_position(port.C, 0)
    while abs(motor.relative_position(port.C)) < distanceInDegrees:
        current_yaw_position = motion_sensor.tilt_angles()[0]
        adjusted = int(round(-0.3 * current_yaw_position)) # tilt_angles are in decidegrees (degrees * 10)
        try:
            motor_pair.move_for_degrees(motor_pair.PAIR_1, 10, adjusted, velocity=-int(round(speed/100.0*660.0)))
        except(ValueError):
            print('value error: ', adjusted)
            motor_pair.move_for_degrees(motor_pair.PAIR_1, 10, int(round(adjusted / 3)), velocity=-int(round(speed/100.0*660.0)))
    motor_pair.stop(motor_pair.PAIR_1)

async def turnRight(degrees):
    await init_drive()
    current_yaw_position = motion_sensor.tilt_angles()[0]
    while current_yaw_position < degrees:
        motor_pair.move_for_degrees(motor_pair.PAIR_1, 1, 100)
        current_yaw_position = motion_sensor.tilt_angles()[0]

async def turnLeft(degrees):
    await init_drive()
    current_yaw_position = motion_sensor.tilt_angles()[0]
    while current_yaw_position > degrees:
        motor_pair.move_for_degrees(motor_pair.PAIR_1, -1, 100)
        current_yaw_position = motion_sensor.tilt_angles()[0]

if __name__ == "__main__":
    runloop.run(backward(50, 50))
    import sys
    sys.exit()