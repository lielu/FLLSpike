
# Generated code
export_code: str = """
import runloop, time
from attachment import *
from drive import *

from hub import port

async def run_blue():
    await forward(47, 100)
    await turnLeft(49)
    await forward(61, 100)
    await forward(10, 50)
    await frontLeft(int(6.5 * 360), 100)
    await backward(5, 80)
    await turnLeft(2)
    await backward(63, 100)
    await turnRight(48)
    await backward(50, 100)

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
