
# Generated code
export_code: str = """
import runloop, time
from attachment import *
from drive import *

from hub import port


#START WITH RIGHT BUMPER ON 1ST THICK LINE FROM RIGHT
async def run_green():
    await forward(10, 50)
    await turnLeft(45)
    await forward(40, 50)
    time.sleep(0.5)
    await forward()



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
