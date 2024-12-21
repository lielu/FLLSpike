import runloop, time
from attachment import *
from drive import *

from hub import port

async def runacross():
    #starts with letft bumper at fourth bold line on left side of board
    await forward(119, 50)
    await backward(10, 100)
    await frontRight(360, 100)
    await forward(70, 100)
    import sys
    sys.exit 

async def food():
    await frontRight(50, 100)

if __name__ == "__main__": 
    runloop.run(runacross())
    #runloop.run(food())
    import sys
    sys.exit()