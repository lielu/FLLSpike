import runloop, time
from attachment import *
from drive import *

from hub import motion_sensor, port, button



async def run_grey():
<<<<<<< HEAD
    # Navigate to squid
    await frontLeft(2*360, 100)
    runloop.run(forward(30, 100), frontLeft(int(80*1.2), 100))
    await frontRight(2*360, 100)
    await turnLeft(50)

    # Drop squid into basket
    await forward(6, 30)

    #COLLECTION + Squid: STARTS AT THE SECOND TO LAST THIN LINE FROM THE RIGHT
    await frontRight(140, 100)
    await backward(20, 100)
    await turnRight(35)
    await frontLeft(2*360, 100)
    await forward(35, 50)
    await frontRight(360, 100)
    await turnRight(35)
    await frontLeft(2*360, 100)
    await forward(6, 50)
    await frontRight(4*360, 100)
    await backward(10, 100)
    await frontRight(360, 100)
    await turnLeft(60)
=======
    #COLLECTION + Squid: STARTS AT FIRST THIN LINE AFTER SECOND BOLD LINE FROM THE RIGHT, CLAW ALL THE WAY OPEN
    #BEGIN COLLECT KRILL
    await forward(40, 100)
    await turnLeft(15)
    await forward(20, 80)
    await frontRight(450, 100)
    await turnRight(60)
    await frontLeft(360, 100)
    await forward(4, 100)
    #CLOSE CLAW TO SECURE KRILL
    await frontRight(720, 100)
    #NAVIGATE TO SONAR DISCOVERY
    await backward(5, 100)
    await turnLeft(40)
    await forward(16, 60)
    #LOWER ARM
    await rearRight(370, 100)
    #MOVE BACK TO SOLVE SONAR DISCOVERY
    await backward(25, 40)
    #NAVIGATE TO OCTOPUS
    runloop.run(rearLeft(362, 100), frontRight(100, 100), backward(35, 90))
    await turnLeft(45)
    #SOLVE OCTOPUS
    await forward(15, 40)
    #BRING OCTOPUS HOME
>>>>>>> 2af8d9f649363ef3f7376357d9b324bdc3f7c9e7
    await backward(70, 100)

    while not button.pressed(button.LEFT):
        motion_sensor.reset_yaw(0)
    
    # 15 is better and more consistent
    await backward(14, 15)
    await forward(15, 100)

    import sys
    sys.exit()

async def food():
    await frontLeft(45, 100)

if __name__ == "__main__":
    runloop.run(run_grey())
    # runloop.run(food())
    import sys
    sys.exit()