# Library Documentation
## Supporting Modules for Spike
Spike Python doesn't provide native support for modules, so we need to create a solution to generate the library Python files when running at a particular slot, then in the main run code import the module from the generated Python file(s). This document explains the process of creating, testing, and generating the library Python files. It also explains the process at competitions and how we make sure the library code is correctly generated and used.

## Creating and Testing Library Code
In typical Python, a library is a file with `.py` extension that contains functions and classes that can be imported and used in other Python code. In the world of FLL Spike, however, a library is also defined in its LLSP3 format. For example, we have a library for the robot driving and turning, which is developed and saved to `src/libs/drive.llsp3`, that contains functions and classes to control the robot movement.

### Sample Library Code
The vanilla `drive.llsp3` library code would have the following structure:
```Python
import motor
from hub import port

async def straight(distance, speed):
    # Code to drive straight with given distance and speed

async def turn(angle, speed):
    # Code to turn with given angle and speed

async def stop():
    # Code to stop the robot
```

### Testing the library code
We'll add a `run_test()` function to the end of the library code to test the library.
```Python
def run_test():
    import runloop
    runloop.run(straight(100, 50))

import sys
run_test()
sys.exit(0)
```
You'll notice that there is no way to import the library into other modules, due to the actual Python code is not exposed to other modules.

## Sharing Library Code
After the library code is tested and ready, we can generate and copy the library file(s) at runtime to root `/flash` folder, so that it can be imported and used in other modules. To do this, a `export_code` string will hold the library source code, and a `exportProgram()` function will be called to generate the library file and copy it to root `/flash` folder with an exported library name.

We modify the above library code to include the code to export the library file to root `/flash` folder.
```Python
# Library code string using python multiline quotes. Do not include test code, only the functions you want to reuse and the imports they need.

export_code: str = """ # uncomment to export program
import motor
from hub import port

async def straight(distance, speed):
    # Code to drive straight with given distance and speed

async def turn(angle, speed):
    # Code to turn with given angle and speed

async def stop():
    # Code to stop the robot
""" # uncomment to export program

def exportProgram(): # Function to export the library code string
     import os
     global export_code
     os.chdir('/flash') # change directory to root
     try:
         os.remove('drive.py') # remove any existing library file of the same name
     except:
         pass
     f = open('drive.py', 'w+') # Create a new file drive.py in the SPIKE hub root
     f.write(export_code) # Write out the library code string to the drive.py file
     f.close()

import sys
exportProgram() # Runs the export function    
sys.exit(0)
```
## Importing Library in Main Code
At runtime, after the library file has been generated to root `/flash` folder, we can import and use the library in any other modules.

```Python
import os
import sys
from drive import *
import runloop

runloop.run(straight(100, 50))
sys.exit(0)
```

## References
The library export method has been documented at https://primelessons.org/en/PyProgrammingLessons/SP3ImportingCustomLibrariesPython.pdf.