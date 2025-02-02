
# Generated code
export_code: str = """
import runloop, time
from attachment import *
from drive import *

from hub import port, button



async def run_grey():
    #COLLECTION + Squid: STARTS AT FIRST THIN LINE AFTER SECOND BOLD LINE FROM THE RIGHT, CLAW ALL THE WAY OPEN
    #BEGIN COLLECT KRILL
    await forward(40, 100)
    await turnLeft(15)
    await forward(20, 80)
    await frontRight(450, 100)
    await turnRight(60)
    await frontLeft(360, 100)
    await forward(4, 100)
    #CLOSE CLAW TO SECURE KRILL
    await frontRight(720, 100)
    #NAVIGATE TO SONAR DISCOVERY
    await backward(5, 100)
    await turnLeft(40)
    await forward(16, 60)
    #LOWER ARM
    await rearRight(370, 100)
    #MOVE BACK TO SOLVE SONAR DISCOVERY
    await backward(25, 40)
    #NAVIGATE TO OCTOPUS
    runloop.run(rearLeft(362, 100), frontRight(100, 100), backward(40, 90))
    await turnLeft(45)
    #SOLVE OCTOPUS
    await forward(17, 40)
    #BRING OCTOPUS HOME
    await backward(70, 100)
    import sys
    sys.exit()

async def food():
    await frontLeft(45, 100)

if __name__ == "__main__":
    runloop.run(run_grey())
    # runloop.run(food())
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
