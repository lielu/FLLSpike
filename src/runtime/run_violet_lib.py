
# Generated code
export_code: str = """
import runloop
from drive import *
from attachment import *
import time

from hub import port


async def run_violet():
    await forward(29, 50)
    await frontLeft(80, 50)
    await forward(5,25)
    await frontLeft(38, 50)
    await forward(21, 50)
    await frontRight(40, 50)
    await backward(40, 50)
    

    

if __name__ == "__main__":
    runloop.run(run_violet())
    import sys
    sys.exit()

"""

def exportProgram():  # Function to export the library code string
    import os
    global export_code
    os.chdir('/flash')  # change directory to root
    try:
        os.remove('run_violet.py')  # remove any existing library file of the same name
    except:
        pass
    f = open('run_violet.py', 'w+')  # Create a new file drive.py in the SPIKE hub root
    f.write(export_code)  # Write out the library code string to the drive.py file
    f.close()

if __name__ == "__main__":
    import sys
    exportProgram()  # Runs the export function    
    sys.exit(0)
