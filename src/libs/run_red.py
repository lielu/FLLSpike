import runloop
from drive import *
from attachment import *
from hub import button
import time

from hub import port
async def run_red():
    #don't start until we press a button
    while not (button.pressed(button.LEFT) or button.pressed(button.RIGHT)):
        pass
 
    #check for button press
    if button.pressed(button.RIGHT):
        #solve the first 3 missions
        await domission_1_2_4()
    elif button.pressed(button.LEFT):
        #code to solve the tree and scuba diver
        await do_tree()
        while not (button.pressed(button.LEFT) or button.pressed(button.RIGHT)):
            pass
        await do_scuba()

async def do_tree():
    await forward(29, 50)
    await frontLeft(80, 50)
    await forward(5,25)
    await frontLeft(40, 70)
    await forward(21, 50)
    await frontRight(52, 50)
    await backward(40, 50)

async def do_scuba():
    print(motor.relative_position(port.A))
    motor.reset_relative_position(port.A,0)
    print(motor.relative_position(port.A))
    print(motor.relative_position(port.A))
    await frontLeft(72, 5)
    await forward(85, 70)
    await turnLeft(89)
    await forward(12, 30)
    await frontLeft(50, 50)
    await backward (10,100)
    await turnRight (85)
    await backward (65, 100)
    await turnRight (45)
    await backward (20, 100)

async def domission_1_2_4():
    await forward(40, 50)
    await turnRight(90)
    await forward(37, 70)
    await backward(15, 50)
    await turnLeft(80)
    await forward(35, 70)
    await turnLeft(98)
    await forward(17, 70)
    await backward(15, 50)
    await turnRight(30)
    await forward(35, 50)
    await backward(8, 70)
    await turnRight(48)
    #await backward(13, 50)
    #await turnRight(19)
    #await forward (3, 50)
    #await frontLeft(1600, 100)
    #await frontRight(1600, 100)
    await backward(45, 100)
    await turnRight(55)
    await backward (45, 100)

if __name__ == "__main__":
    runloop.run(run_red())
    import sys
    sys.exit()
    