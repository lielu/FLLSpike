
# Generated code
export_code: str = """
import runloop
from drive import *


from hub import port

async def main():
    await forward(50, 50)
    await turnLeft(45)
    await forward(37, 50)
    await turnLeft(95)
    await forward(30, 50)
    await backward(15, 50)
    await turnRight(30)
    await forward(40, 100)
    await backward(13, 50)
    await turnRight(47)
    await backward(45, 50)
    await turnRight(55)
    await backward (45, 50)

if __name__ == "__main__":
    runloop.run(main())
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
