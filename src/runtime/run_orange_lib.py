
# Generated code
export_code: str = """
import runloop
from drive import *
from attachment import *
import time

from hub import port


async def run_orange():
    await forward(30, 70)
    await turnRight(43)
    await forward(40, 70)
    await turnRight(50)
    await forward(30, 70)
    await frontLeft(360, 85)
    await frontRight(360, 50)
    await backward(30, 100)
    await turnLeft(45)
    await backward(45, 100)
    await turnLeft(45)
    await backward(37, 100)



if __name__ == "__main__":
    runloop.run(run_orange())
    import sys
    sys.exit()
"""

def exportProgram():  # Function to export the library code string
    import os
    global export_code
    os.chdir('/flash')  # change directory to root
    try:
        os.remove('run_orange.py')  # remove any existing library file of the same name
    except:
        pass
    f = open('run_orange.py', 'w+')  # Create a new file drive.py in the SPIKE hub root
    f.write(export_code)  # Write out the library code string to the drive.py file
    f.close()

if __name__ == "__main__":
    import sys
    exportProgram()  # Runs the export function    
    sys.exit(0)
