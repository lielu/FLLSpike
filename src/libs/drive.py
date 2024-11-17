from hub import port, motion_sensor
import motor #imports a ability to control a single motor
import motor_pair #imports a pair of motors moving like one
import runloop

motor_speed = 1100
async def movebydistance(distance, speed):
    global current_yaw_position, distanceInDegrees # Global variables: available outside of function
    distanceInDegrees = distance / 17.5 * 360#Sets how far the motor should turn in degrees
    motor.reset_relative_position(port.C, 0) #Sets the relative position to 0 so we can track its rotations
    while motor.relative_position(port.C) < distanceInDegrees: #repeats the following code until it has moved far enough
        current_yaw_position = motion_sensor.tilt_angles()[0]#Sets yaw position to 0
        adjusted = int(round(0.3 * current_yaw_position)) # tilt_angles are in decidegrees (degrees * 10)
        #rotate by 60 degrees unless we're less than 60 degrees from target
        rotation=60 if distanceInDegrees-motor.relative_position(port.C)> 60 else distanceInDegrees-motor.relative_position(port.C)
        print(rotation)
        try: #attempts to try this
            await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(rotation), adjusted, velocity=int(round(speed/100.0*motor_speed)), stop=motor.CONTINUE) #Move forward 60 degrees, check again
        except(ValueError):#This runs if the robot finds that the value is too big(100, -100)
            print('value error: ', adjusted)#Prints if finds error
            await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(rotation), int(round(adjusted / 3)), velocity=int(round(speed/100.0*motor_speed)), stop=motor.CONTINUE) # Reduces turn amount so no value error
            # Goes to the line just under " while motor.relative…"

async def movebytime(time, speed):
    runtime=0
    while runtime < time*1000: #repeats the following code until it has moved far enough
        current_yaw_position = motion_sensor.tilt_angles()[0]#Sets yaw position to 0
        runtime = runtime + 200
        adjusted = int(round(0.3 * current_yaw_position)) # tilt_angles are in decidegrees (degrees * 10)
        await motor_pair.move_for_time(motor_pair.PAIR_1, 200, adjusted, velocity=int(round(speed/100.0*motor_speed)), stop=motor.CONTINUE)
    #motor_pair.stop(motor_pair.PAIR_1)


distanceInDegrees = 0
current_yaw_position = 0#Sets yaw position to 0

async def init_drive(port1, port2):
    motor_pair.unpair(motor_pair.PAIR_1) #Unpair first or it will encounter an error later.
    motor_pair.pair(motor_pair.PAIR_1, port1, port2) #Motor pair called motor_pair.PAIR_1, left motor: port D, right motor: port C
    motion_sensor.reset_yaw(0) #Makes the robot think its facing forward.
    runloop.until(motion_sensor.stable)

async def forward(value, speed, mode = 'distance'): #FUNCTION
    await init_drive(port.D, port.C)#Waits for init_drive() to initialize
    if mode == 'distance':
        await movebydistance(value, speed)
    else:
        await movebytime(value, speed)
    motor_pair.stop(motor_pair.PAIR_1)#stops motor after done with distance

async def backward(value, speed, mode='distance'): #Basically the same as the first code, but the motors are reversed, thus giving us reverse action
    await init_drive(port.C, port.D) # Reverse motors
    if mode == 'distance':
        await movebydistance(value, speed)
    else:
        await movebytime(value, speed)
    motor_pair.stop(motor_pair.PAIR_1)#stops motor after done with distance

async def turnbydegrees(degrees, mod):
    current_yaw_position = abs(motion_sensor.tilt_angles()[0])
    while current_yaw_position < degrees* 10:
        #print(str(current_yaw_position) + ":" +str(degrees*10) )
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, mod, 100, stop=motor.CONTINUE)
        current_yaw_position = abs(motion_sensor.tilt_angles()[0])

async def turnbytime(time, mod):
    await motor_pair.move_for_time(motor_pair.PAIR_1, time * 1000, mod * 100) #turn for small amount

async def turnRight(value, mode='degrees'): #Function for turn right code
    await init_drive(port.D, port.C) # Waits for initiation
    if mode=='degrees':
        await turnbydegrees(value, 1)
    else:
        await turnbytime(value, 1)

async def turnLeft(value, mode='degrees'): #same as right, only left
    await init_drive(port.D, port.C)
    if mode=='degrees':
        await turnbydegrees(value, -1)
    else:
        await turnbytime(value, -1)


async def test_drive(): #test code for drive functions

    #await init_drive(port.D, port.C)
    await turnRight(90, 'degrees')
    #await motor_pair.move_for_time(motor_pair.PAIR_1, 5000, 0, velocity=int(round(100/100.0*1100.0)))

if __name__ == "__main__":
    runloop.run(test_drive())
    import sys#Imports Sys so we can exit code
    sys.exit()#Exits out of code
