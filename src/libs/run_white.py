import runloop, time
from attachment import *
from drive import *

from hub import port

async def run_white():
    # starts with left bumper at fourth bold line on left edge of board, left arm all the way up with shark loosely inside
    # bring arm down
    await rearRight(340, 100)

    # move boat across
    await forward(39, 100) # approach boat
    await turnLeft(1) # slow
    await forward(10, 40) # engage at lower speed
    await turnLeft(6) # turn to compensate
    await forward(39, 90) # goes to shark drop zone
    await rearLeft(90, 100) # raises to release shark
    await forward(39, 90) # run boat to other dock
    await backward(10, 100) # release boat
    await frontRight(360, 100) # raise arm so boat can stay
    await forward(80, 100) # run to end, total distance was 127

async def food():
    await frontRight(360, 100)

if __name__ == "__main__": 
    runloop.run(run_white())
    #runloop.run(food())
    import sys
    sys.exit()