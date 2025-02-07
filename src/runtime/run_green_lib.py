
# Generated code
export_code: str = """
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
    await backward(32, 100)
    await turnLeft(90)
    await backward(70, 100)
    
if __name__ == "__main__":
    runloop.run(run_green())
    import sys
    sys.exit()
"""

def exportProgram():  # Function to export the library code string
    import os
    global export_code
    os.chdir('/flash')  # change directory to root
    try:
        os.remove('run_green.py')  # remove any existing library file of the same name
    except:
        pass
    f = open('run_green.py', 'w+')  # Create a new file drive.py in the SPIKE hub root
    f.write(export_code)  # Write out the library code string to the drive.py file
    f.close()

if __name__ == "__main__":
    import sys
    exportProgram()  # Runs the export function    
    sys.exit(0)
