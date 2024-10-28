
# Generated code
export_code: str = """
from hub import port, motion_sensor
import motor #imports a ability to control a single motor
import motor_pair #imports a pair of motors moving like one
import runloop

distanceInDegrees = 0
current_yaw_position = 0#Sets yaw position to 0

async def init_drive(port1, port2):
    motor_pair.unpair(motor_pair.PAIR_1) #Unpair first or it will encounter an error later.
    motor_pair.pair(motor_pair.PAIR_1, port1, port2) #Motor pair called motor_pair.PAIR_1, left motor: port D, right motor: port C
    motion_sensor.reset_yaw(0) #Makes the robot think its facing forward.
    runloop.until(motion_sensor.stable)

async def forward(distance, speed): #FUNCTION
    await init_drive(port.D, port.C)#Waits for init_drive() to initialize
    global current_yaw_position, distanceInDegrees # Global variables: available outside of function
    distanceInDegrees = distance / 17.5 * 360#Sets how far the motor should turn in degrees
    motor.reset_relative_position(port.C, 0) #Sets the relative position to 0 so we can track its rotations
    while motor.relative_position(port.C) < distanceInDegrees: #repeats the following code until it has moved far enough
        current_yaw_position = motion_sensor.tilt_angles()[0]#Sets yaw position to 0
        adjusted = int(round(0.3 * current_yaw_position)) # tilt_angles are in decidegrees (degrees * 10)
        try: #attempts to try this
            motor_pair.move_for_degrees(motor_pair.PAIR_1, 60, adjusted, velocity=int(round(speed/100.0*660.0))) #Move forward 60 degrees, check again
        except(ValueError):#This runs if the robot finds that the value is too big(100, -100)
            print('value error: ', adjusted)#Prints if finds error
            motor_pair.move_for_degrees(motor_pair.PAIR_1, 60, int(round(adjusted / 3)), velocity=int(round(speed/100.0*660.0))) # Reduces turn amount so no value error
            # Goes to the line just under " while motor.relative…"
    motor_pair.stop(motor_pair.PAIR_1)#stops motor after done with distance

async def backward(distance, speed): #Basically the same as the first code, but the motors are reversed, thus giving us reverse action
    await init_drive(port.C, port.D) # Reverse motors
    global current_yaw_position, distanceInDegrees
    distanceInDegrees = distance / 17.5 * 360
    motor.reset_relative_position(port.C, 0)
    while abs(motor.relative_position(port.C)) < distanceInDegrees:
        current_yaw_position = motion_sensor.tilt_angles()[0]
        adjusted = int(round(0.3 * current_yaw_position)) # tilt_angles are in decidegrees (degrees * 10)
        try:
            motor_pair.move_for_degrees(motor_pair.PAIR_1, 60, adjusted, velocity=int(round(speed/100.0*660.0)))
        except(ValueError):
            print('value error: ', adjusted)
            motor_pair.move_for_degrees(motor_pair.PAIR_1, 60, int(round(adjusted / 3)), velocity=int(round(speed/100.0*660.0)))
    motor_pair.stop(motor_pair.PAIR_1)

async def turnRight(degrees): #Function for turn right code
    await init_drive(port.D, port.C) # Waits for initiation
    current_yaw_position = motion_sensor.tilt_angles()[0]# Refreshes variable "current_yaw_position"
    while abs(current_yaw_position) < abs(degrees*10): #abs to make sure both are positive, < so that it stops when it is at the goal
        print(str(degrees) + ", " + str(current_yaw_position)) #Check current degrees
        motor_pair.move_for_degrees(motor_pair.PAIR_1, 10, 100) #turn for small amount
        current_yaw_position = motion_sensor.tilt_angles()[0]# Refreshes variable "current_yaw_position"

async def turnLeft(degrees): #same as right, only left
    await init_drive(port.D, port.C)
    current_yaw_position = motion_sensor.tilt_angles()[0]# Refreshes variable "current_yaw_position"
    while abs(current_yaw_position) < abs(degrees * 10):
        motor_pair.move_for_degrees(motor_pair.PAIR_1, -10, 100)
        current_yaw_position = motion_sensor.tilt_angles()[0]# Refreshes variable "current_yaw_position"

async def test_drive(): #test code for drive functions
    await forward(50, 100)
    await turnLeft(90)
    await backward(50, 100)
    await turnRight(90)

if __name__ == "__main__":
    runloop.run(test_drive())
    import sys#Imports Sys so we can exit code
    sys.exit()#Exits out of code

"""

def exportProgram():  # Function to export the library code string
    import os
    global export_code
    os.chdir('/flash')  # change directory to root
    try:
        os.remove('drive.py')  # remove any existing library file of the same name
    except:
        pass
    f = open('drive.py', 'w+')  # Create a new file drive.py in the SPIKE hub root
    f.write(export_code)  # Write out the library code string to the drive.py file
    f.close()

if __name__ == "__main__":
    import sys
    exportProgram()  # Runs the export function    
    sys.exit(0)
