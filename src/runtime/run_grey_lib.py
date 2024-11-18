
# Generated code
export_code: str = """
import runloop, time
from attachment import *
from drive import *

from hub import port


#START WITH RIGHT BUMPER ON 1ST THICK LINE FROM RIGHT
async def run_grey():
    '''# Navigate to squid
    await forward(10, 50)
    await turnLeft(45)

    # Drop squid into basket
    await forward(40, 50)
    time.sleep(0.5)

    # Navigate to drop zone
    await backward(10, 50)
    await turnLeft(45)
    await forward(50, 50)
    await turnRight(88)

    # Drop and move away
    await forward(20, 50)
    await frontLeft(int(6.5 * 360), 100)
    await backward(12, 50)
    await frontRight((5 * 360), 100)

    # Navigate to home
    await backward(12, 100)
    await turnLeft(86)
    await backward(50, 100)
    await turnRight(48)
    await backward(35, 100)
    await frontRight(int(2 * 360), 100)'''

    '''COLLECTION: STARTS AT THE FIRST THIN LINE AFTER THE SECOND
    THICK LINE'''

    ''' Wait to let person add seperate attatchment + move
    to start position'''

    #time.sleep(5)
    # Navigate to first krill + seewead, pick up

    await frontLeft(4*360, 100)
    await forward(28, 50)
    await turnLeft(15)
    await frontRight(4*360, 100)
    await turnRight(15)
    await backward(25, 100)

    '''await frontLeft(7*360, 100)
    await forward(45, 50)
    await frontRight(4*360, 100)'''

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
