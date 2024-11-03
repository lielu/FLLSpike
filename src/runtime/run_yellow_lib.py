
# Generated code
export_code: str = """
import runloop, time
from attachment import *
from drive import *

from hub import port

async def run_yellow():#Start right back piece on farthest dark line in red square
    #Left raises the arm
    #right lowers the arm
    await frontLeft(int(1.8 * 360), 50)
    
    await forward(65, 50)
    await turnRight(30)
    await forward(14, 20)
    await frontRight(int(3 * 360), 75)
    await frontLeft(int(3 * 360), 50)
    await backward(12, 20)
    await turnLeft(20)
    await backward(75, 100)
    await frontRight(int(2 * 360), 75)


if __name__ == "__main__":
    runloop.run(run_yellow())
    import sys
    sys.exit()
"""

def exportProgram():  # Function to export the library code string
    import os
    global export_code
    os.chdir('/flash')  # change directory to root
    try:
        os.remove('run_yellow.py')  # remove any existing library file of the same name
    except:
        pass
    f = open('run_yellow.py', 'w+')  # Create a new file drive.py in the SPIKE hub root
    f.write(export_code)  # Write out the library code string to the drive.py file
    f.close()

if __name__ == "__main__":
    import sys
    exportProgram()  # Runs the export function    
    sys.exit(0)
