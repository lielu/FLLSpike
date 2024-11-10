
# Generated code
export_code: str = """
import runloop
from drive import *

from hub import port

# Shouldn't be used. Use run_grey instead.

async def main():
    await forward(10, 50)

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
        os.remove('run_black.py')  # remove any existing library file of the same name
    except:
        pass
    f = open('run_black.py', 'w+')  # Create a new file drive.py in the SPIKE hub root
    f.write(export_code)  # Write out the library code string to the drive.py file
    f.close()

if __name__ == "__main__":
    import sys
    exportProgram()  # Runs the export function    
    sys.exit(0)
