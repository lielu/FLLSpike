
# Generated code
export_code: str = """
import runloop, time
from attachment import *
from drive import *

from hub import port

async def run_yellow():
    await frontLeft(int(6.5 * 360), 100)

    await forward(10, 50)
    await turnLeft(42)
    await forward(40, 50)
    time.sleep(0.5)
    await backward(10, 50)
    await turnLeft(48)
    await forward(50, 50)
    await turnRight(92)
    await forward(24, 50)
    await frontLeft(int(6.5 * 360), 100)
    await backward(24, 50)
    await frontRight(int(6.5*360), 100)
    await turnLeft(92)
    await backward(50, 100)
    await turnRight(48)
    await backward(40, 100)
    import sys
    sys.exit()



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
