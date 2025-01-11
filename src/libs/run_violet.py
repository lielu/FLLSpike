import runloop
from drive import *
from attachment import *
import time

from hub import port


async def run_violet():
    await forward(29, 50)
    await frontLeft(80, 50)
    await forward(5,25)
    await frontLeft(38, 50)
    await forward(21, 50)
    await frontRight(40, 50)
    await backward(40, 50)
    

    

if __name__ == "__main__":
    runloop.run(run_violet())
    import sys
    sys.exit()
