import runloop, time
from attachment import *
from drive import *

from hub import port

async def run_grey():
    await forward(10, 50)
    await turnLeft(45)
    await forward(40, 50)
    time.sleep(0.5)
    await backward(10, 50)
    await turnLeft(45)
    await forward(50, 50)
    await turnRight(88)
    await forward(22, 50)
    await frontLeft(int(6.5 * 360), 100)
    await backward(10, 50)
    await frontRight((5 * 360), 100)
    await backward(12, 100)
    await turnLeft(86)
    await backward(50, 100)
    await turnRight(48)
    await backward(40, 100)
    import sys
    sys.exit()



if __name__ == "__main__":
    runloop.run(run_grey())
    import sys
    sys.exit()