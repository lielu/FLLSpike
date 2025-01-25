
# Generated code
export_code: str = """
import runloop, time
from attachment import *
from drive import *

from hub import port

async def run_white():
    # starts with left bumper at fourth bold line on left edge of board, left arm all the way up with shark loosely inside
    # bring arm down
    await rearRight(340, 100)

    # move boat across
    await forward(39, 100) # approach boat
    await turnLeft(1) # slow
    await forward(10, 40) # engage at lower speed
    await turnLeft(6) # turn to compensate
    await forward(39, 90) # goes to shark drop zone
    await rearLeft(90, 100) # raises to release shark
    await forward(39, 90) # run boat to other dock
    await backward(10, 100) # release boat
    await frontRight(360, 100) # raise arm so boat can stay
    await forward(80, 100) # run to end, total distance was 127

async def food():
    await frontRight(360, 100)

if __name__ == "__main__": 
    runloop.run(run_white())
    #runloop.run(food())
    import sys
    sys.exit()
"""

def exportProgram():  # Function to export the library code string
    import os
    global export_code
    os.chdir('/flash')  # change directory to root
    try:
        os.remove('run_white.py')  # remove any existing library file of the same name
    except:
        pass
    f = open('run_white.py', 'w+')  # Create a new file drive.py in the SPIKE hub root
    f.write(export_code)  # Write out the library code string to the drive.py file
    f.close()

if __name__ == "__main__":
    import sys
    exportProgram()  # Runs the export function    
    sys.exit(0)
