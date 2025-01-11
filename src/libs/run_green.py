import runloop, time
from attachment import *
from drive import *

from hub import port


#START WITH RIGHT BUMPER ON 1ST THICK LINE FROM RIGHT
async def run_green():
    await forward(10, 50)
    await turnLeft(45)
    await forward(40, 50)
    time.sleep(0.5)
    await forward()



if __name__ == "__main__":
    runloop.run(run_green())
    import sys
    sys.exit()