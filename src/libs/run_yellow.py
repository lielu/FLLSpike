import runloop, time
from attachment import *
from drive import *

from hub import port

async def run_yellow():#Start right back piece on farthest dark line in red square
    #Left raises the arm
    #right lowers the arm
    await frontLeft(int(1.8 * 360), 50)
    
    await forward(65, 50)
    await turnRight(30)
    await forward(14, 20)
    await frontRight(int(3 * 360), 75)
    await frontLeft(int(3 * 360), 50)
    await backward(12, 20)
    await turnLeft(20)
    await backward(75, 100)
    await frontRight(int(2 * 360), 75)


if __name__ == "__main__":
    runloop.run(run_yellow())
    import sys
    sys.exit()