import runloop
from drive import *
from attachment import *
import time

from hub import port


async def run_orange():
    await forward(30, 50)
    await turnRight(40)
    await forward(40, 50)
    await turnRight(47)
    await forward(30, 50)
    await frontLeft(360, 50)
    await frontRight(360, 50)
    await backward(20, 50)
    await turnLeft(45)
    await backward(45, 50)
    await turnLeft(45)
    await backward(33, 50)



if __name__ == "__main__":
    runloop.run(run_orange())
    import sys
    sys.exit()