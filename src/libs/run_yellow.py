import runloop, time
from attachment import *
from drive import *

from hub import port, button

async def mission3():
    await forward(48, 70)
    await turnLeft(37)
    await forward(37, 70)
    time.sleep(0.2)
    await forward(5, 100)
    await frontRight(int(6 * 360), 70)
    await frontLeft(int(2.5 * 360), 70)
    await backward(50, 100)
    await turnRight(37)
    await backward(35, 100)

async def collecting():
    await forward(30, 100)
    await turnLeft(27)
    await forward(33, 100)
    await frontRight(int(1 * 360), 50)
    await backward(40, 100)
    await turnRight(45)
    await backward(35, 100)

async def run_yellow():
    while not (button.pressed(button.LEFT) or button.pressed(button.RIGHT)):
        pass
    #right and left are inverted based on how our hub faces
    if button.pressed(button.RIGHT): #left button
        runloop.run(mission3())
    elif button.pressed(button.LEFT): #right button
        runloop.run(collecting())


if __name__ == "__main__":
    runloop.run(run_yellow())
    import sys
    sys.exit()