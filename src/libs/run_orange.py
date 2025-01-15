import runloop
from drive import *
from attachment import *
import time

from hub import port


async def run_orange():
    await forward(30, 70)
    await turnRight(43)
    await forward(40, 70)
    await turnRight(50)
    await forward(30, 70)
    await frontLeft(360, 85)
    await frontRight(360, 50)
    await backward(30, 100)
    await turnLeft(45)
    await backward(45, 100)
    await turnLeft(45)
    await backward(37, 100)



if __name__ == "__main__":
    runloop.run(run_orange())
    import sys
    sys.exit()