
# Generated code
export_code: str = """
import runloop, time
from attachment import *
from drive import *

from hub import port, button



async def run_grey():
    # Navigate to squid
    await frontLeft(2*360, 100)
    runloop.run(forward(30, 100), frontLeft(int(80*1.2), 100))
    await frontRight(2*360, 100)
    await turnLeft(50)

    # Drop squid into basket
    await forward(6, 30)

    #COLLECTION + Squid: STARTS AT THE SECOND TO LAST THIN LINE FROM THE RIGHT
    await frontRight(140, 100)
    await backward(20, 100)
    await turnRight(35)
    await frontLeft(2*360, 100)
    await forward(35, 50)
    await frontRight(360, 100)
    await turnRight(35)
    await forward(6, 50)
    await frontRight(4*360, 100)
    await backward(10, 100)
    await frontRight(360, 100)
    await turnLeft(60)
    await backward(70, 100)
    
    import sys
    sys.exit()

async def food():
    await frontLeft(45, 100)

if __name__ == "__main__":
    runloop.run(run_grey())
    # runloop.run(food())
    import sys
    sys.exit()
"""

def exportProgram():  # Function to export the library code string
    import os
    global export_code
    os.chdir('/flash')  # change directory to root
    try:
        os.remove('run_grey.py')  # remove any existing library file of the same name
    except:
        pass
    f = open('run_grey.py', 'w+')  # Create a new file drive.py in the SPIKE hub root
    f.write(export_code)  # Write out the library code string to the drive.py file
    f.close()

if __name__ == "__main__":
    import sys
    exportProgram()  # Runs the export function    
    sys.exit(0)
