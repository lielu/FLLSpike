
# Generated code
export_code: str = """
import runloop, time
from attachment import *
from drive import *

from hub import port, button



async def run_grey():
    #COLLECTION: STARTS AT THE SECOND TO LAST THIN LINE FROM THE RIGHT
    await frontLeft(int(70*2), 100)
    runloop.run(frontLeft(int(80*1.2), 100), forward(25, 50))
    await forward(30, 50)
    await frontRight(int(150*1.2), 100)
    await turnRight(15)
    await frontLeft(int(150*1.2), 100)
    await forward(13, 100)
    await frontRight(int(360*2), 100)
    await backward(30, 100)
    await turnLeft(45)
    await backward(55, 100)

    # Wait to let person add move to start position
    while not button.pressed(button.LEFT):
        pass

    await forward(30, 50)
    await turnLeft(30)
    await forward(40, 50)
    await turnRight(30)
    await forward(8, 50)
    await turnRight(70)
    await frontLeft(int(6.5*360), 100)
    await forward(10, 100)
    await frontRight(7*360, 100)
    await backward(15, 100)
    await turnRight(90)
    await forward(40, 100)
    await turnLeft(30, 100)
    await froward(40, 100)

    #START WITH LEFT BUMBER ON SECOND TO LAST THIN LINE FROM RIGHT
    while not button.pressed(button.LEFT):
        pass

    # Navigate to squid
    await frontLeft(int(70*1.2), 100)
    runloop.run(forward(25, 50), frontLeft(int(80*1.2)))
    await turnLeft(45)

    # Drop squid into basket
    await forward(14, 15)
    time.sleep(0.5)

    # Navigate home
    await frontRight(2*360, 100)
    await backward(20, 100)
    await turnRight(45)
    await frontRight(1*360, 100)
    await backward(30, 100)

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
