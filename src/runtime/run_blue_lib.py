
# Generated code
export_code: str = """
import runloop, time
from attachment import *
from drive import *

from hub import port
#Robot left edge aligned with fourth thin line from left, end pushing to the wall#
async def run_blue():
    await forward(42, 100)
    await turnLeft(49)
    await forward(61, 100)
    await forward(5, 20)
    #arives at the submarine
<<<<<<< HEAD
    await frontLeft(int(6.9 * 360), 100)
    await backward(7, 80)
=======
    await frontLeft(int(6.7 * 360), 100)
    time.sleep(2) # keep the submarine in position
    runloop.run(frontLeft(int(-6.7 * 360), 100), backward(9, 80)) # back off and lower arm at the same time
>>>>>>> 2af8d9f649363ef3f7376357d9b324bdc3f7c9e7
    await turnLeft(67)
    await forward(28, 100)
    await turnRight(65)
<<<<<<< HEAD
    await backward(4, 50)
=======
    # await backward(2, 100) # doesn't seem like robot needs to move
>>>>>>> 2af8d9f649363ef3f7376357d9b324bdc3f7c9e7
    #finshes anglerfish


if __name__ == "__main__":
    runloop.run(run_blue())
    import sys
    sys.exit()
"""

def exportProgram():  # Function to export the library code string
    import os
    global export_code
    os.chdir('/flash')  # change directory to root
    try:
        os.remove('run_blue.py')  # remove any existing library file of the same name
    except:
        pass
    f = open('run_blue.py', 'w+')  # Create a new file drive.py in the SPIKE hub root
    f.write(export_code)  # Write out the library code string to the drive.py file
    f.close()

if __name__ == "__main__":
    import sys
    exportProgram()  # Runs the export function    
    sys.exit(0)
