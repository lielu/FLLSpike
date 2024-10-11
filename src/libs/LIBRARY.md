# Sharing Library Modules for FLL Spike Robotics

## Overview
This document outlines the process of creating libraries for Spike Prime and installing them at runtime using the automated tools provided in this repository.

## Prerequisites
- Spike app installed on your computer. Or you can choose to use the [web-based Spike IDE](https://spike.legoeducation.com/) instead.
- Python 3.10 or later installed on your computer.
- Clone this repository to your computer. If you have already cloned it previously, make sure it is up to date by pulling the latest changes from the repository by running `git pull` in the terminal.
- Follow the instructions in the [README.md](../README.md#saving-llsp3-and-python-files-into-github) file and start monitoring the LLSP3 files to Python code changes.

### macOS
```sh
cd <your-local-repo-folder>/FLLSpike/utils
python3 monitor_llsp3_to_python_mac.py start --directory <your-local-repo-folder>/FLLSpike/src
```
### Windows
```sh
cd <your-local-repo-folder>/FLLSpike/utils
python monitor_llsp3_to_python_win.py start --directory <your-local-repo-folder>/FLLSpike/src
```

## Creating a Library

When you need to create a new library, follow these steps:
1. Use Spike to create a Spike Prime library that will be imported and called by other Spike modules. For example, for driving functions, create a `drive` project in Spike and save it to the `src/libs/` directory. This will create a `drive.llsp3` file.
2. Write your library code as normal Python functions and classes. Make sure the functions and classes are properly documented with parameter descriptions. Use the [drive.py](drive.py) file as a template:
```Python
from hub import port, motion_sensor
import motor #imports a ability to control a single motor
import motor_pair #imports a pair of motors moving like one
import runloop

distanceInDegrees = 0
current_yaw_position = 0

async def init_drive():
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C) #Motor pair called motor_pair.PAIR_1, left motor: port D, right motor: port C
    motion_sensor.reset_yaw(0) #Makes the robot think its facing forward.
    runloop.until(motion_sensor.stable)

async def forward(distance, speed): #FUNCTION
    await init_drive()
    # TODO: Implement the forward function

# other functions...

# Include test code within an if __name__ == "__main__" block to make sure the library works as expected
if __name__ == "__main__":
    runloop.run(forward(50, 50))
    import sys
    sys.exit() 
```

3. Test the library code by running the `drive.llsp3` file in Spike app. 
4. When testing is done, the library can be imported and used in other modules. Add the library name `<library-name>.py` to the `monitored_libraries` list in the [monitor_llsp3_to_python_mac.py](../Utils/monitor_llsp3_to_python_mac.py) or [monitor_llsp3_to_python_win.py](../Utils/monitor_llsp3_to_python_win.py) file if it's not already there.
5. You may need to restart the LLSP3 monitor tools by running `python monitor_llsp3_to_python_mac.py start --directory <your-local-repo-folder>/FLLSpike/src/libs` or `python monitor_llsp3_to_python_win.py start --directory <your-local-repo-folder>/FLLSpike/src/libs` in the terminal to pick up the new library.

## Automated Library Generation

The LLSP3 monitor tools will automatically generate a Python library and LLSP3 file for importing the library. For example, when the `drive.py` file is modified, the LLSP3 monitor tools will generate a `drive_lib.py` and `drive_lib.llsp3` files in `src/libs/runtime/` directory. To import and use the library in other modules, follow the steps:
1. Open the `src/runtime/drive_lib.llsp3` file in Spike app, and `Run` the code when a Spike Prime hub is connected to the Spike app. The library will be installed in the Spike hub (at the `/flash` folder), and can be imported and used in other modules.
2. In a `main_code` module, it can import the library using `from <library-name> import *` and use the library functions as normal. For example:

```Python
    from drive import *
    
    await forward(50, 50)
```
Please note that the Spike app will not recognize the imported functions and provide calling suggestions. This is fine as long as the library code is correctly generated.

## Installing Libraries at Competition

At competition, to prepare for the runs, make sure all the library files are installed in the Spike hub. Follow these steps to properly install the libraries (it should be done the night before the competition):

1. Run `git pull` before the competition and make sure all generated library files are in the `src/libs/runtime/` directory.
2. Open Spike app, load each of the LLSP3 library files in the `src/libs/runtime/` directory one by one, and verify the library code is correctly loaded and it's the latest version.
3. Connect to the Spike hub and run each LLSP3 library file. 
4. Load the run code LLSP3 files, and verify they run correctly for each mission. 

## Extra Reading
### Supporting Modules for Spike
Spike Python doesn't provide native support for modules, so we need to create a solution to generate the library Python files that can be imported and used in other modules at runtime.

### Creating and Testing Library Code
In typical Python, a library is a file with `.py` extension that contains functions and classes that can be imported and used in other Python code. In the world of FLL Spike, however, a library is also defined in its LLSP3 format. For example, we have a library for the robot driving and turning, which is developed and saved to `src/libs/drive.llsp3`, that contains functions and classes to control the robot movement. You can find the example drive code included in the previous section.

### Sharing Library Code
After the library code is tested and ready, one approach is to generate the Python code exactly the same as the library code that we've developed in the LLSP3 file, and install the Python file into Spike hub file system so that other modules can import and use it at runtime. In our LLSP3 monitoring tools, it has been automated to create another LLSP3 file whose only purpose is to copy the library source code into LLSP3 and install it as a Python file in Spike hub file system (in the `/flash` directory). By doing this, we are able to allow other modules to import the library file at runtime and call their functions.

### References
The library export method has been documented at https://primelessons.org/en/PyProgrammingLessons/SP3ImportingCustomLibrariesPython.pdf.