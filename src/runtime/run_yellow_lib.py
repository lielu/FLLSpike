
# Generated code
export_code: str = """
import runloop, time
from attachment import *
from drive import *

from hub import port, button

async def collector():
    runloop.run(frontLeft(int(2.4 * 360), 50), forward(30, 70))
    await turnLeft(28)
    await forward(40, 60)
    await frontRight(int(3 * 360), 50)
    await backward(40, 60)
    await turnRight(45)
    await backward(35, 70)

async def domission3():
    #### MOVE TO MISSION 3 ####
    runloop.run(frontLeft(int(1.8 * 360), 50), forward(65, 50)) #Lowers arm

    #await forward(65, 50) #Moves robot straight toward mission 3
    await turnRight(28) #Turns first turn to straighten out robot toward mission 3
    await forward(14, 20)#Slowly moves to mission 3
    #### END MOVE TO MISSION 3 ####

    #### SOLVE MISSION 3 ####
    await frontRight(int(6 * 360), 75) #Lowers arm to solve mission
    await frontLeft(int(3 * 360), 50) #Lifts arm not to bump into anything
    await backward(8, 35) #Backs away from mission
    #### END SOLVE MISSION 3 ####

async def return_from_mission3():
    await backward(12, 20) #Starts to bring back to home
    await turnLeft(20)
    await backward(75, 100)
    await frontRight(int(2 * 360), 75)
#async def run_yellow():#Start right back piece on farthest dark line in red square
    #Left raises the arm
    #right lowers the arm
    #### MOVE TO MISSION 3 ####
    runloop.run(frontLeft(int(1.8 * 360), 50), forward(65, 50)) #Lowers arm

    #await forward(65, 50) #Moves robot straight toward mission 3
    await turnRight(28) #Turns first turn to straighten out robot toward mission 3
    await forward(14, 20)#Slowly moves to mission 3
    #### END MOVE TO MISSION 3 ####

    #### SOLVE MISSION 3 ####
    await frontRight(int(6 * 360), 75) #Lowers arm to solve mission
    await frontLeft(int(3 * 360), 50) #Lifts arm not to bump into anything
    await backward(8, 35) #Backs away from mission
    #### END SOLVE MISSION 3 ####

    await turnRight(45) #Ligns up to solve mission 11
    await forward(70, 80)
    await turnRight(22)
    await forward(35, 75)
    await turnLeft(55)
    await backward(7, 20)
    await frontRight(int(3 * 360), 75) #Puts arm in position
    #### READY TO SOLVE MISSION 11 ####
    await forward(7, 50)
    await frontLeft(int(4 * 360), 60) #Lifts arm to solve one whale
    await backward(12, 40)
    await turnRight(45)
    await forward(45, 75)
    await turnLeft(80)
    await forward(8, 20) #Aligns to second whale
    await turnLeft(25)
    await frontRight(int(4 * 360), 75)
    #### SOLVING 2ND PART OF MISSION 11 ####
    await turnRight(45)
    await backward(50, 50) #Starting to go back to blue circle
    #return_from_mission3()

async def mission3():
    await forward(48, 70)
    await turnLeft(37)
    await forward(37, 70)
    time.sleep(0.2)
    await forward(5, 70)
    await frontRight(int(6 * 360), 50)
    await frontLeft(int(3 * 360), 50)
    await backward(10, 70)
    await turnRight(30)
    await backward(50, 70)
    await turnLeft(45)
    await backward(20, 70)

async def collecting():
    await forward(30, 100)
    await turnLeft(32)
    await forward(33, 100)
    await frontRight(int(1.5 * 360), 50)
    await backward(40, 100)
    await turnRight(45)
    await backward(25, 100)

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
