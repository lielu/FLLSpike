import runloop, time
from attachment import *
from drive import *

from hub import port, button



async def run_grey():
    # Navigate to squid
    await frontLeft(2*360, 100)
    runloop.run(forward(30, 50), frontLeft(int(80*1.2), 100))
    await frontRight(2*360, 100)
    await turnLeft(50)

    # Drop squid into basket
    await forward(9, 20)

    #COLLECTION + Squid: STARTS AT THE SECOND TO LAST THIN LINE FROM THE RIGHT
    await frontRight(140, 100)
    await backward(20, 50)
    await turnRight(30)
    await frontLeft(2*360, 100)
    await forward(40, 50)
    await frontRight(360, 100)
    await turnRight(45)
    await frontLeft(140, 100)
    await forward(6, 50)
    await frontRight(4*360, 100)
    await backward(10, 100)
    await frontRight(360, 100)
    await turnRight(70)
    await backward(30, 100)
    await turnLeft(100)
    await backward(40, 100)
    
    import sys
    sys.exit()

async def food():
    await frontLeft(45, 100)

if __name__ == "__main__":
    runloop.run(run_grey())
    # runloop.run(food())
    import sys
    sys.exit()