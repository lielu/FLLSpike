import runloop, time
from attachment import *
from drive import *

from hub import port
async def return_from_mission3():
    await backward(12, 20) #Starts to bring back to home
    await turnLeft(20)
    await backward(75, 100)
    await frontRight(int(2 * 360), 75) 
async def run_yellow():#Start right back piece on farthest dark line in red square
    #Left raises the arm
    #right lowers the arm
    await frontLeft(int(1.8 * 360), 50) #Lowers arm
    
    await forward(65, 50) #Moves robot straight toward mission 3
    await turnRight(30) #Turns first turn to straighten out robot toward mission 3
    await forward(12, 20)
    await frontRight(int(3 * 360), 75)
    await frontLeft(int(3 * 360), 50) #Lowers arm to solve mission
    await backward(10, 35)
    await turnRight(45) #Ligns up to solve mission 11
    await forward(70, 80)
    await turnRight(22)
    await forward(30, 75)
    await turnLeft(60)
    await backward(7, 20)
    await frontRight(int(3 * 360), 75) #Puts arm in position
    await forward(7, 50)
    await frontLeft(int(2 * 360), 60) #Lifts arm to solve one whale
    await backward(12, 40)
    await turnRight(45)
    await forward(40, 75) 
    await turnLeft(90)
    await forward(5, 20) #Aligns to second whale
    await turnLeft(25)
    await frontRight(int(2 * 360), 75)
    await backward(20, 50) #Starting to go back to blue circle
    #return_from_mission3()    


if __name__ == "__main__":
    runloop.run(run_yellow())
    import sys
    sys.exit()