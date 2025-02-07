import runloop, time
from attachment import *
from drive import *

from hub import port
#Robot left edge aligned with fourth thin line from left, end pushing to the wall#
async def run_blue():
    await forward(42, 100)
    await turnLeft(49)
    await forward(53, 100)
    await forward(10, 20)
    #arives at the submarine
    await frontLeft(int(6.7 * 360), 100)
    time.sleep(2) # keep the submarine in position
    runloop.run(frontLeft(int(-6.7 * 360), 100), backward(9, 80)) # back off and lower arm at the same time
    await turnLeft(67)
    await forward(20, 70)
    await turnRight(65)
    # await backward(2, 100) # doesn't seem like robot needs to move
    #finshes anglerfish


if __name__ == "__main__":
    runloop.run(run_blue())
    import sys
    sys.exit()