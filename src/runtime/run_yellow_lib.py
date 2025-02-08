
# Generated code
export_code: str = """
import runloop, time
from attachment import *
from drive import *

from hub import port, button

async def mission3():
    await forward(48, 70)
    await turnLeft(37)
    await forward(37, 70)
    time.sleep(0.2)
    await forward(5, 100)
    await frontRight(int(6 * 360), 70)
    await frontLeft(int(2.5 * 360), 70)
    await backward(50, 100)
    await turnRight(37)
    await backward(35, 100)

async def collecting():
    await forward(30, 100)
    await turnLeft(27)
    await forward(33, 100)
    await frontRight(int(1 * 360), 50)
    await backward(40, 100)
    await turnRight(45)
    await backward(35, 100)

async def run_yellow():
    while not (button.pressed(button.LEFT) or button.pressed(button.RIGHT)):
        pass
    #right and left are inverted based on how our hub faces
    if button.pressed(button.RIGHT): #left button
        runloop.run(mission3())
    elif button.pressed(button.LEFT): #right button
        runloop.run(collecting())


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
