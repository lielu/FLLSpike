import runloop, time
from attachment import *
from drive import *

from hub import port, button



async def run_grey():
    
    #COLLECTION + Squid: STARTS AT FIRST THIN LINE AFTER SECOND BOLD LINE FROM THE RIGHT, CLAW ALL THE WAY OPEN
    #BEGIN COLLECT KRILL
    await forward(37, 100)
    await turnLeft(15)
    await forward(20, 60)
    await frontRight(720, 100)
    await turnRight(49)
    await frontLeft(720, 100)
    await forward(6, 60)
    #CLOSE CLAW TO SECURE KRILL
    await frontRight(720, 100)
    #NAVIGATE TO SONAR DISCOVERY
    await backward(3, 100)
    await turnLeft(35)
    time.sleep(0.08)
    await forward(1, 60, mode = 'time')
    #LOWER ARM
    await rearRight(370, 100)
    #MOVE BACK TO SOLVE SONAR DISCOVERY
    await backward(25, 40)
    #NAVIGATE TO OCTOPUS
    runloop.run(rearLeft(362, 100), frontRight(100, 100), backward(33, 90))
    await turnLeft(55)
    #SOLVE OCTOPUS
    await forward(1, 50, mode = 'time')
    #BRING OCTOPUS HOME
    await backward(55, 100)

    # while not button.pressed(button.LEFT):
    #     motion_sensor.reset_yaw(0)

    # # 15 is better and more consistent
    # await backward(14, 15)
    # await forward(15, 100)

    import sys
    sys.exit()
async def food():
    await frontLeft(45, 100)

if __name__ == "__main__":
    runloop.run(run_grey())
    # runloop.run(food())
    import sys
    sys.exit()