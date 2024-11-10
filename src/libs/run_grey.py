import runloop, time
from attachment import *
from drive import *

from hub import port


#START WITH RIGHT BUMPER ON 1ST THICK LINE FROM RIGHT
async def run_grey():
    '''# Navigate to squid
    await forward(10, 50)
    await turnLeft(45)
    
    # Drop squid into basket
    await forward(40, 50)
    time.sleep(0.5)

    # Navigate to drop zone
    await backward(10, 50)
    await turnLeft(45)
    await forward(50, 50)
    await turnRight(88)

    # Drop and move away
    await forward(22, 50)
    await frontLeft(int(6.5 * 360), 100)
    await backward(10, 50)
    await frontRight((5 * 360), 100)

    # Navigate to home
    await backward(12, 100)
    await turnLeft(86)
    await backward(50, 100)
    await turnRight(48)
    await backward(35, 100)
    await frontRight(int(2 * 360), 100)'''

    # COLLECT 3 KRILL: STARTS IN SAME PLACE AS BEGINNING
    ''' Wait to let person add seperate attatchment + move
    to start position'''
    
    #time.sleep(3)
    # Navigate to first krill + seewead, pick up
    '''await forward(13, 50)
    await turnLeft(15)
    await frontLeft(int(6.5*360), 100)
    await forward(30, 50)
    await frontRight(3*360, 100)
    await backward(5, 50)
    await frontRight(int(3.5*360), 100)
    await backward(25, 100)
    await turnRight(22)
    await backward(13, 100)'''


    import sys
    sys.exit()

if __name__ == "__main__":
    runloop.run(run_grey())
    import sys
    sys.exit()