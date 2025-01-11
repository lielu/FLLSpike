
# Generated code
export_code: str = """
import runloop, time
from attachment import *
from drive import *

from hub import port

async def run_white():
    #starts with letft bumper at fourth bold line on left edge of board
    #move boat across
    await forward(119, 50)
    await backward(10, 100)
    await frontRight(360, 100)
    await forward(70, 100)
    import sys
    sys.exit 

async def food():
    await frontRight(50, 100)

if __name__ == "__main__": 
    runloop.run(runacross())
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
