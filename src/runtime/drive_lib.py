
# Generated code
export_code: str = """
# Drive code
# initiate drive: prepares robot to drive by assigning motors, reseting sensors
# forward/backward by degrees: uses relative postition of one drive motor, uses yaw sensor to make robot drive straight
# turn right and left by degrees: turns with yaw sensor
# 
from hub import port, motion_sensor # port allows to connect to other things, motion sensor includes yaw sensor
import motor #imports a ability to control a single motor
import motor_pair #imports a pair of motors moving like one
import runloop # Allows function to run simutaneously like in normal scratch

motor_speed = 1100 # Tells the code the top speed a motor can go
distanceInDegrees = 0 # Defines a distance for later use
current_yaw_position = 0#Sets yaw position to 0

async def init_drive(port1, port2):
    motor_pair.unpair(motor_pair.PAIR_1) #Unpair first or it will encounter an error later.
    motor_pair.pair(motor_pair.PAIR_1, port1, port2) #Motor pair called motor_pair.PAIR_1, left motor: port D, right motor: port C
    motion_sensor.reset_yaw(0) #Makes the robot think its facing forward.
    runloop.until(motion_sensor.stable) # waits until the motion sensor senses the hub is stable

async def forwardByDegrees(distance, speed): #uses relative postition of one drive motor, uses yaw sensor to make robot drive straight
    await init_drive(port.D, port.C)#Waits for init_drive() to initialize - connect to driving motors and reset yaw to 0
    global current_yaw_position, distanceInDegrees # Global variables: available outside of function
    distanceInDegrees = distance / 17.5 * 360#Sets how far the motor should turn in degrees - 1 rotation = 17.5 cm
    motor.reset_relative_position(port.C, 0) #Sets the relative position of the motor C to 0 so we can track its rotations
    while motor.relative_position(port.C) < distanceInDegrees: #repeats the following code until it has moved far enough
        current_yaw_position = motion_sensor.tilt_angles()[0]#Sets current yaw position to variable. LEFT = POSITIVE 0 to 300. RIGHT = NEGATIVE 0 to -300
        adjusted = int(round(0.3 * current_yaw_position)) # tilt_angles are in decidegrees (degrees * 10) - this will drive robot the opposite way. LEFT = NEGATIVE and RIGHT = POSITIVE.
        #rotate 60 degrees or the remaining degrees to our distance, whichever is smaller
        rotation=60 if distanceInDegrees-abs(motor.relative_position(port.C))> 60 else distanceInDegrees-abs(motor.relative_position(port.C))
        try: #attempts to try this
            motor_pair.move_for_degrees(motor_pair.PAIR_1, int(rotation), adjusted, velocity=int(round(speed/100.0*motor_speed))) #Move forward 60 degrees, check again
            # LIPIN PAUSE
        except(ValueError):#This runs if the robot finds that the value is too big(100, -100)
            #print('value error: ', adjusted)##prints if finds error
            motor_pair.move_for_degrees(motor_pair.PAIR_1, int(rotation), int(round(adjusted / 3)), velocity=int(round(speed/100.0*motor_speed))) # Reduces turn amount so no value error
            # Goes to the line just under " while motor.relative…"
    motor_pair.stop(motor_pair.PAIR_1)#stops motor after done with distance

async def backwardByDegrees(distance, speed): #Basically the same as the first code, but the motors are reversed, thus giving us reverse action
    await init_drive(port.C, port.D) # Reverse motors
    global current_yaw_position, distanceInDegrees
    distanceInDegrees = distance / 17.5 * 360
    motor.reset_relative_position(port.C, 0)
    while abs(motor.relative_position(port.C)) < distanceInDegrees:
        current_yaw_position = motion_sensor.tilt_angles()[0]
        adjusted = int(round(0.3 * current_yaw_position)) # tilt_angles are in decidegrees (degrees * 10)
        #rotate 60 degrees or the remaining degrees to our distance, whichever is smaller
        rotation=60 #if distanceInDegrees-abs(motor.relative_position(port.C))> 60 else distanceInDegrees-abs(motor.relative_position(port.C))
        try:
            motor_pair.move_for_degrees(motor_pair.PAIR_1, int(rotation), adjusted, velocity=int(round(speed/100.0*motor_speed)))
        except(ValueError):
            #print('value error: ', adjusted)
            motor_pair.move_for_degrees(motor_pair.PAIR_1, int(rotation), int(round(adjusted / 3)), velocity=int(round(speed/100.0*motor_speed)))
    motor_pair.stop(motor_pair.PAIR_1)

async def turnRightByDegrees(degrees): #Function for turn right code
    await init_drive(port.D, port.C) # Waits for initiation
    current_yaw_position = motion_sensor.tilt_angles()[0]# Refreshes variable "current_yaw_position"
    while abs(current_yaw_position) < abs(degrees*10): #abs to make sure both are positive, < so that it stops when it is at the goal
        #print(str(degrees) + ", " + str(current_yaw_position)) #Check current degrees
        motor_pair.move_for_degrees(motor_pair.PAIR_1, 10, 100) #turn for small amount
        current_yaw_position = motion_sensor.tilt_angles()[0]# Refreshes variable "current_yaw_position"

async def turnLeftByDegrees(degrees): #same as right, only left
    await init_drive(port.D, port.C)
    current_yaw_position = motion_sensor.tilt_angles()[0]# Refreshes variable "current_yaw_position"
    while abs(current_yaw_position) < abs(degrees * 10):
        motor_pair.move_for_degrees(motor_pair.PAIR_1, -10, 100)
        current_yaw_position = motion_sensor.tilt_angles()[0]# Refreshes variable "current_yaw_position"

async def movebytime(time, speed):
    runtime=0
    while runtime < time*1000: #repeats the following code until it has moved far enough
        current_yaw_position = motion_sensor.tilt_angles()[0]#Sets yaw position to 0
        runtime = runtime + 200
        adjusted = int(round(0.3 * current_yaw_position)) # tilt_angles are in decidegrees (degrees * 10)
        await motor_pair.move_for_time(motor_pair.PAIR_1, 200, adjusted, velocity=int(round(speed/100.0*motor_speed)), stop=motor.CONTINUE)
    #motor_pair.stop(motor_pair.PAIR_1)

async def forward(value, speed, mode = 'distance'): #FUNCTION
    await init_drive(port.D, port.C)#Waits for init_drive() to initialize
    if mode == 'distance':
        await forwardByDegrees(value, speed)
    else:
        await movebytime(value, speed)
    motor_pair.stop(motor_pair.PAIR_1)#stops motor after done with distance

async def backward(value, speed, mode='distance'): #Basically the same as the first code, but the motors are reversed, thus giving us reverse action
    await init_drive(port.C, port.D) # Reverse motors
    if mode == 'distance':
        await backwardByDegrees(value, speed)
    else:
        await movebytime(value, speed)
    motor_pair.stop(motor_pair.PAIR_1)#stops motor after done with distance

async def turnbytime(time, mod):
    await motor_pair.move_for_time(motor_pair.PAIR_1, time * 1000, mod * 100, stop=motor.COAST) #turn for small amount
    motor.stop(motor_pair.PAIR_1)

async def turnRight(value, mode='degrees'): #Function for turn right code
    await init_drive(port.D, port.C) # Waits for initiation
    if mode=='degrees':
        await turnRightByDegrees(value)
    else:
        await turnbytime(value, 1)

async def turnLeft(value, mode='degrees'): #same as right, only left
    await init_drive(port.D, port.C)
    if mode=='degrees':
        await turnLeftByDegrees(value)
    else:
        await turnbytime(value, -1)

async def test_drive(): #test code for drive functions
    await forwardByDegrees(50, 50)
    '''
    await turnRight(5, 'time')
    await forward(10,50)
    await turnLeft(5, 'time')
    await backward(10,50)
    await turnRight(5, 'time')'''

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
