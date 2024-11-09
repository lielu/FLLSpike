
# Generated code
export_code: str = """
import runloop, time
from attachment import *
from drive import *

from hub import port


#START WITH RIGHT BUMPER ON 1ST THICK LINE FROM RIGHT
async def run_grey():
    await forward(10, 50)
    await turnLeft(45)
    await forward(40, 50)
    time.sleep(0.5)
    await backward(10, 50)
    await turnLeft(45)
    await forward(50, 50)
    await turnRight(88)
    await forward(22, 50)
    await frontLeft(int(6.5 * 360), 100)
    await backward(10, 50)
    await frontRight((5 * 360), 100)
    await backward(12, 100)
    await turnLeft(86)
    await backward(50, 100)
    await turnRight(48)
    await backward(35, 100)
    await frontRight(int(2 * 360), 100)

    # COLLECT 3 KRILL: STARTS IN SAME PLACE AS BEGINNING

    time.sleep(2.5)
    await forward(20, 50)
    await turnLeft(29)
    await frontLeft(3 * 360, 100)
    await forward(14, 50)
    await frontRight(550, 100)
    await turnRight(21.5)
    await forward(27, 50)
    await turnRight(35)
    await frontLeft(350, 100)
    await forward(10, 50)
    await frontRight(3 * 360 - 200, 100)
    await backward(10, 100)
    await turnLeft(45)
    await backward(60, 100)
    import sys
    sys.exit()



if __name__ == "__main__":
    runloop.run(run_grey())
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
