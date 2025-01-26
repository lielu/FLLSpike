import runloop, time
from attachment import *
from drive import *

from hub import port
#Robot left edge aligned with fourth thin line from left, end pushing to the wall#
async def run_blue():
    await forward(40, 100)
    await turnLeft(50)
    await forward(61, 100)
    await forward(10, 50)
    #arives at the submarine
    await frontLeft(int(6.7 * 360), 100)
    time.sleep(2)
    # await frontLeft(int(-6.7 * 360), 100)
    await backward(7, 80)
    await turnLeft(67)
    await forward(25, 70)
    await turnRight(65)
    await backward(2, 100)
    #finshes anglerfish


if __name__ == "__main__":
    runloop.run(run_blue())
    import sys
    sys.exit()