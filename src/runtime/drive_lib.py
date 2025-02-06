
# Generated code
export_code: str = """
from hub import port, motion_sensor
import motor #imports a ability to control a single motor
import motor_pair #imports a pair of motors moving like one
import runloop

motor_speed = 1100
distanceInDegrees = 0
current_yaw_position = 0#Sets yaw position to 0

async def init_drive(port1, port2):
    motor_pair.unpair(motor_pair.PAIR_1) #Unpair first or it will encounter an error later.
    motor_pair.pair(motor_pair.PAIR_1, port1, port2) #Motor pair called motor_pair.PAIR_1, left motor: port D, right motor: port C
    motion_sensor.reset_yaw(0) #Makes the robot think its facing forward.
    runloop.until(motion_sensor.stable)

async def forwardByDegrees(distance, speed): #FUNCTION
    await init_drive(port.D, port.C)#Waits for init_drive() to initialize
    global current_yaw_position, distanceInDegrees, motor_speed # Global variables: available outside of function
    distanceInDegrees = distance / 17.5 * 360#Sets how far the motor should turn in degrees
    motor.reset_relative_position(port.C, 0) #Sets the relative position to 0 so we can track its rotations
    while motor.relative_position(port.C) < distanceInDegrees: #repeats the following code until it has moved far enough
        current_yaw_position = motion_sensor.tilt_angles()[0]#Sets yaw position to 0
        adjusted = int(round(0.3 * current_yaw_position)) # tilt_angles are in decidegrees (degrees * 10)
        #rotate 60 degrees or the remaining degrees to our distance, whichever is smaller
        rotation=30 if distanceInDegrees-abs(motor.relative_position(port.C))> 30 else distanceInDegrees-abs(motor.relative_position(port.C))
        try: #attempts to try this
            motor_pair.move_for_degrees(motor_pair.PAIR_1, int(rotation), adjusted, velocity=int(round(speed/100.0*motor_speed)), stop=motor.CONTINUE) #Move forward 60 degrees, check again
        except(ValueError):#This runs if the robot finds that the value is too big(100, -100)
            #print('value error: ', adjusted)##prints if finds error
            motor_pair.move_for_degrees(motor_pair.PAIR_1, int(rotation), int(round(adjusted / 3)), velocity=int(round(speed/100.0*motor_speed)), stop=motor.CONTINUE) # Reduces turn amount so no value error
            # Goes to the line just under " while motor.relative…"
    motor_pair.stop(motor_pair.PAIR_1, stop=motor.SMART_BRAKE)#stops motor after done with distance

async def backwardByDegrees(distance, speed): #Basically the same as the first code, but the motors are reversed, thus giving us reverse action
    await init_drive(port.C, port.D) # Reverse motors
    global current_yaw_position, distanceInDegrees, motor_speed
    distanceInDegrees = distance / 17.5 * 360
    motor.reset_relative_position(port.C, 0)
    while abs(motor.relative_position(port.C)) < distanceInDegrees:
        current_yaw_position = motion_sensor.tilt_angles()[0]
        adjusted = int(round(0.3 * current_yaw_position)) # tilt_angles are in decidegrees (degrees * 10)
        #rotate 60 degrees or the remaining degrees to our distance, whichever is smaller
        rotation=30 if distanceInDegrees-abs(motor.relative_position(port.C))> 30 else distanceInDegrees-abs(motor.relative_position(port.C))
        try:
            motor_pair.move_for_degrees(motor_pair.PAIR_1, int(rotation), adjusted, velocity=int(round(speed/100.0*motor_speed)), stop=motor.CONTINUE)
        except(ValueError):
            #print('value error: ', adjusted)
            motor_pair.move_for_degrees(motor_pair.PAIR_1, int(rotation), int(round(adjusted / 3)), velocity=int(round(speed/100.0*motor_speed)), stop=motor.CONTINUE)
    motor_pair.stop(motor_pair.PAIR_1, stop=motor.SMART_BRAKE)

async def turnRightByDegrees(degrees): #Function for turn right code
    await init_drive(port.D, port.C) # Waits for initiation
    current_yaw_position = motion_sensor.tilt_angles()[0]# Refreshes variable "current_yaw_position"
    while abs(current_yaw_position) < abs(degrees*10): #abs to make sure both are positive, < so that it stops when it is at the goal
        #print(str(degrees) + ", " + str(current_yaw_position)) #Check current degrees
        motor_pair.move_for_degrees(motor_pair.PAIR_1, 10, 100, stop=motor.CONTINUE) #turn for small amount
        current_yaw_position = motion_sensor.tilt_angles()[0]# Refreshes variable "current_yaw_position"
    motor_pair.stop(motor_pair.PAIR_1, stop=motor.SMART_BRAKE)

async def turnLeftByDegrees(degrees): #same as right, only left
    await init_drive(port.D, port.C)
    current_yaw_position = motion_sensor.tilt_angles()[0]# Refreshes variable "current_yaw_position"
    while abs(current_yaw_position) < abs(degrees * 10):
        motor_pair.move_for_degrees(motor_pair.PAIR_1, -10, 100, stop=motor.CONTINUE)
        current_yaw_position = motion_sensor.tilt_angles()[0]# Refreshes variable "current_yaw_position"
    motor_pair.stop(motor_pair.PAIR_1, stop=motor.SMART_BRAKE)

async def movebytime(time, speed):
    global motor_speed
    runtime=0
    while runtime < time*1000: #repeats the following code until it has moved far enough
        current_yaw_position = motion_sensor.tilt_angles()[0]#Sets yaw position to 0
        runtime = runtime + 200
        adjusted = int(round(0.3 * current_yaw_position)) # tilt_angles are in decidegrees (degrees * 10)
        await motor_pair.move_for_time(motor_pair.PAIR_1, 200, adjusted, velocity=int(round(speed/100.0*motor_speed)), stop=motor.CONTINUE)
    #motor_pair.stop(motor_pair.PAIR_1)

async def forward(value, speed, mode = 'distance'): #FUNCTION
    global motor_speed
    await init_drive(port.D, port.C)#Waits for init_drive() to initialize
    if mode == 'distance':
        await forwardByDegrees(value, speed)
    else:
        await movebytime(value, speed)
    motor_pair.stop(motor_pair.PAIR_1)#stops motor after done with distance

async def backward(value, speed, mode='distance'): #Basically the same as the first code, but the motors are reversed, thus giving us reverse action
    global motor_speed
    await init_drive(port.C, port.D) # Reverse motors
    if mode == 'distance':
        await backwardByDegrees(value, speed)
    else:
        await movebytime(value, speed)
    motor_pair.stop(motor_pair.PAIR_1)#stops motor after done with distance

async def turnbytime(time, mod):
    global motor_speed
    await motor_pair.move_for_time(motor_pair.PAIR_1, time * 1000, mod * 100, stop=motor.COAST) #turn for small amount
    motor.stop(motor_pair.PAIR_1)

async def turnRight(value, mode='degrees'): #Function for turn right code
    global motor_speed
    await init_drive(port.D, port.C) # Waits for initiation
    if mode=='degrees':
        await turnRightByDegrees(value)
    else:
        await turnbytime(value, 1)

async def turnLeft(value, mode='degrees'): #same as right, only left
    global motor_speed
    
    await init_drive(port.D, port.C)
    if mode=='degrees':
        await turnLeftByDegrees(value)
    else:
        await turnbytime(value, -1)

async def test_drive(): #test code for drive functions
    await turnRight(5, 'time')
    await forward(10,50)
    await turnLeft(5, 'time')
    await backward(10,50)
    await turnRight(5, 'time')

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
