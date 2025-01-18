import runloop, time
from attachment import *
from drive import *

from hub import port

async def run_white():
    #starts with letft bumper at fourth bold line on left edge of board
    #move boat across
    await forward(39, 100) #approach boat
    await turnLeft(1) #slow
    await forward(10, 50) #engage at lower speed
    await turnLeft(5) #turn to compensate
    await forward(78, 90) #run to end, total distance was 127
    await backward(10, 90)
    await frontRight(360, 100)
    await forward(80, 90)

async def food():
    await frontRight(360, 100)

if __name__ == "__main__": 
    runloop.run(run_white())
    #runloop.run(food())
    import sys
    sys.exit()