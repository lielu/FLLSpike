
# Generated code
export_code: str = """
import runloop, time
from attachment import *
from drive import *

from hub import port
#Put robot outer shell 1/4 way from first bold line from inside of mat#
async def run_blue():
    runloop.run(frontLeft(int(-6.5 * 360), 100), forward(40, 100))
    await turnLeft(50)
    await forward(61, 100)
    await forward(10, 50)
    await frontLeft(int(6.9 * 360), 100)
    await backward(7, 80)
    await turnLeft(67)
    await forward(28, 100)
    await turnRight(45)
    await backward(20, 100)
    await turnLeft(45)
    await backward(12, 100)  
    await turnRight(90)
    await backward(40, 100)
    await turnRight(30)
    await backward(100, 100)

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
