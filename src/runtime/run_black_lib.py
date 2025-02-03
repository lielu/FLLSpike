
# Generated code
export_code: str = """
import runloop
from drive import *
from attachment import *

from hub import port

# Shouldn't be used. Use run_grey instead.

# Start 45 degree at the right side corner
async def main():
    await forward(30, 70)
    await turnRight(43)
    await forward(40, 70)
    await turnRight(46)
    await forward(20, 40)
    await frontLeft(450, 85)
    await backward(30, 100)
    await turnLeft(90)
    await backward(70, 100)

    # Submarine and anglerfish
    # await forward(42, 100)
    # await turnLeft(49)
    # back up now from whale
    await bachward(40, 80)
    await turnRight(90)

    # await forward(61, 100)
    # await forward(5, 20)
    # back up now to mash into submarine
    await backward(61, 100)
    await backward(5, 20)

    #arives at the submarine
    # await frontLeft(int(6.7 * 360), 100)
    # using the rear motor
    await rearLeft(int(6.7 * 360), 100)

    time.sleep(2) # keep the submarine in position
    # runloop.run(frontLeft(int(-6.7 * 360), 100), backward(9, 80)) # back off and lower arm at the same time
    runloop.run(rearLeft(int(-6.7 * 360), 100), forward(9, 80)) # back off and lower arm at the same time

    # await turnLeft(67)
    # await forward(25, 70)
    # await turnRight(65)
    await turnRight(67)
    await backward(25, 70)
    await turnLeft(65)
    
    # await backward(2, 100) # doesn't seem like robot needs to move
    #finshes anglerfish

if __name__ == "__main__":
    runloop.run(main())
    import sys
    sys.exit()
"""

def exportProgram():  # Function to export the library code string
    import os
    global export_code
    os.chdir('/flash')  # change directory to root
    try:
        os.remove('run_black.py')  # remove any existing library file of the same name
    except:
        pass
    f = open('run_black.py', 'w+')  # Create a new file drive.py in the SPIKE hub root
    f.write(export_code)  # Write out the library code string to the drive.py file
    f.close()

if __name__ == "__main__":
    import sys
    exportProgram()  # Runs the export function    
    sys.exit(0)
