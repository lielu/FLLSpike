import runloop, time
from attachment import *
from drive import *

from hub import port


#START WITH LEFT BUMBER ON SECOND TO LAST THIN LINE FROM RIGHT
def run_grey_2():
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