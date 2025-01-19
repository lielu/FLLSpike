import runloop, time
from attachment import *
from drive import *

from hub import port


# Replace run_orange to be the whale mission
# Start 45 degree at the right side corner
async def run_green():
    await forward(30, 70)
    await turnRight(43)
    await forward(40, 70)
    await turnRight(46)
    await forward(20, 40)
    await frontLeft(450, 85)
    await backward(30, 100)
    await turnLeft(90)
    await backward(70, 100)
    
if __name__ == "__main__":
    runloop.run(run_green())
    import sys
    sys.exit()