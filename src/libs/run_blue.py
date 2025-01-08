import runloop, time
from attachment import *
from drive import *

from hub import port
#Put robot outer shell 1/4 way from first bold line from inside of mat#
async def run_blue():
    runloop.run(frontLeft(int(-6.5 * 360), 100), forward(40, 100))
    await turnLeft(50)
    await forward(61, 100)
    await forward(10, 50)
    #arives at the submarine
    await frontLeft(int(6.9 * 360), 100)
    await backward(7, 80)
    await turnLeft(67)
    await forward(28, 100)
    await turnRight(65)
    await backward(4, 50)
    #finshes anglerfish


if __name__ == "__main__":
    runloop.run(run_blue())
    import sys
    sys.exit()