
# Generated code
export_code: str = """
import runloop
from drive import *
from attachment import *
from hub import button
import time

from hub import port
async def run_red():
    #don't start until we press a button
    while not (button.pressed(button.LEFT) or button.pressed(button.RIGHT)):
        pass

    #check for button press
    if button.pressed(button.RIGHT):
        #solve the first 3 missions
        await domission_1_2_4()
    elif button.pressed(button.LEFT):
        #code to solve the tree and scuba diver
        # await do_tree()
        # while not (button.pressed(button.LEFT) or button.pressed(button.RIGHT)):
        #    pass
        await do_scuba()

async def do_tree():
    await forward(29, 50)
    await frontLeft(80, 50)
    await forward(5,25)
    await frontLeft(40, 70)
    await forward(21, 50)
    await frontRight(52, 50)
    await backward(40, 50)

async def do_scuba():
    await forward(50, 100)
    await frontLeft(120, 50)
    time.sleep(0.2)
    await backward(50, 100)
    await frontRight(120, 50)

async def domission_1_2_4():
    await forward(40, 50)
    await turnRight(90)
    await forward(37, 70)
    await backward(15, 50)
    await turnLeft(80)
    await forward(35, 70)
    await turnLeft(98)
    await forward(17, 70)
    await backward(15, 50)
    await turnRight(30)
    await forward(35, 50)
    await backward(8, 70)
    await turnRight(48)
    #await backward(13, 50)
    #await turnRight(19)
    #await forward (3, 50)
    #await frontLeft(1600, 100)
    #await frontRight(1600, 100)
    await backward(45, 100)
    await turnRight(55)
    await backward (45, 100)

if __name__ == "__main__":
    runloop.run(run_red())
    import sys
    sys.exit()

"""

def exportProgram():  # Function to export the library code string
    import os
    global export_code
    os.chdir('/flash')  # change directory to root
    try:
        os.remove('run_red.py')  # remove any existing library file of the same name
    except:
        pass
    f = open('run_red.py', 'w+')  # Create a new file drive.py in the SPIKE hub root
    f.write(export_code)  # Write out the library code string to the drive.py file
    f.close()

if __name__ == "__main__":
    import sys
    exportProgram()  # Runs the export function    
    sys.exit(0)
