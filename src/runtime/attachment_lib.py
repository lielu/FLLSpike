
# Generated code
export_code: str = """
from hub import port
from motor import run_for_degrees
import runloop

async def frontRight(degrees, speed):
    await run_for_degrees(port.A, degrees, int(round(speed / 100 * -1050)))

async def frontLeft(degrees, speed):
    await run_for_degrees(port.A, degrees, int(round(speed / 100 * 1050)))

async def rearLeft(degrees, speed):
    await run_for_degrees(port.F, degrees, int(round(speed / 100 * 1050)))

async def rearRight(degrees, speed):
    await run_for_degrees(port.F, degrees, int(round(speed / 100 * -1050)))

async def test_attachment(): #test code for drive functions
    await frontRight(360, 100)
    await frontLeft(360, 100)
    await rearRight(360, 100)
    await rearLeft(360, 100)

if __name__ == "__main__":
    runloop.run(test_attachment())
    import sys #Imports Sys so we can exit code
    sys.exit() #Exits out of code
"""

def exportProgram():  # Function to export the library code string
    import os
    global export_code
    os.chdir('/flash')  # change directory to root
    try:
        os.remove('attachment.py')  # remove any existing library file of the same name
    except:
        pass
    f = open('attachment.py', 'w+')  # Create a new file drive.py in the SPIKE hub root
    f.write(export_code)  # Write out the library code string to the drive.py file
    f.close()

if __name__ == "__main__":
    import sys
    exportProgram()  # Runs the export function    
    sys.exit(0)
