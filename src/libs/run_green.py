import runloop, time
from attachment import *
from drive import *

from hub import port


#START WITH RIGHT BUMPER ON 1ST THICK LINE FROM RIGHT
async def run_green():
    await forward(65, 50)
    await turnRight(50)
    await forward(45, 50)
    await turnLeft(20)
    await backward(50,40)
    await turnRight(80)





if __name__ == "__main__":
    runloop.run(run_green())
    import sys
    sys.exit()