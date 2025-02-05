import runloop, time
from attachment import *
from drive import *

from hub import port
async def shark_trident():
    
    await rearRight(int(2 * 360), 50)
    time.sleep(0.4)
    await forward(8, 60)
    runloop.run(rearLeft(int(1.5 * 360), 50), forward(25, 70))
    await frontRight(100, 100)
async def food():
    await frontRight(360, 100)

async def forward_and_turn(distance):
    for i in range(distance/20):
        await forward(distance/20, 80)
        #await turnLeft(2)
    

async def run_white():
    #starts with letft bumper at fourth bold line on left edge of board
    #move boat across
    await frontRight(60  , 100)
    #return
    await forward(40, 60) #approach boat and lift arm slightly
    await turnLeft(3) #slow
    await forward(83, 80) #engage at lower speed
    #await turnLeft(5) #turn to compensate
    #await forward(5, 50)
    #time.sleep(0.1) #run to end, total distance was 127
    #await turnLeft(16)
    #await forward_and_turn(90)
    #await turnLeft(10)
    await backward(10, 90) #Back away from the ship
    await frontRight(80, 100) #raise the arm
    await turnLeft(5) #adjust position 
    await backward(22, 75) # back up to the trident
    await shark_trident()
    await turnRight(20) #repoint to the home
    await forward(80, 90)


if __name__ == "__main__": 
    runloop.run(run_white())
    #runloop.run(food())
    import sys
    sys.exit()