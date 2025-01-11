import runloop, time
from attachment import *
from drive import *

from hub import port



async def run_grey():
    #COLLECTION: STARTS AT THE SECOND TO LAST THIN LINE FROM THE RIGHT
    await frontLeft(int(70*1.2), 100)
    runloop.run(frontLeft(int(80*1.2), 100), forward(25, 50))
    await forward(30, 50)
    await frontRight(int(150*1.2), 100)
    await turnRight(15)
    await frontLeft(int(150*1.2), 100)
    await forward(15, 100)
    await frontRight(int(360*1.2), 100)
    await backward(30, 100)
    await turnLeft(25)
    await backward(50, 100)
    
    # Wait to let person add move to start position
    time.sleep(5)

    #START WITH LEFT BUMBER ON SECOND TO LAST THIN LINE FROM RIGHT

    # Navigate to squid
    await forward(25, 50)
    await turnLeft(45)

    # Drop squid into basket
    await forward(14, 15)
    time.sleep(0.5)

    # Navigate to drop zone
    await backward(10, 50)
    await turnLeft(45)
    await forward(50, 50)
    await turnRight(88)

    # Drop and move away
    await forward(20, 50)
    await frontLeft(int(6.5 * 360), 100)
    await backward(12, 50)
    await frontRight((5 * 360), 100)

    # Navigate to home
    await backward(12, 100)
    await turnLeft(86)
    await backward(50, 100)
    await turnRight(48)
    await backward(35, 100)
    await frontRight(int(2 * 360), 100)

    import sys
    sys.exit()

async def food():
    await frontLeft(45, 100)

if __name__ == "__main__":
    runloop.run(run_grey())
    # runloop.run(food())
    import sys
    sys.exit()