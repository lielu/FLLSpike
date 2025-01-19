import runloop, time
from attachment import *
from drive import *

from hub import port, button



async def run_grey():
    '''# Navigate to squid
    await frontLeft(2*360, 100)
    runloop.run(forward(30, 100), frontLeft(int(80*1.2), 100))
    await frontRight(2*360, 100)
    await turnLeft(50)

    # Drop squid into basket
    await forward(6, 30)'''

    #COLLECTION + Squid: STARTS AT THE SECOND TO LAST THIN LINE FROM THE RIGHT
    await frontLeft(2*360, 100)
    await forward(55, 100)
    await turnRight(15)
    await forward(10, 100)
    await frontRight(4*360, 100)
    await backward(5, 100)
    await turnLeft(15)
    await frontRight(200, 100)
    await backward(40, 100)
    await turnLeft(40)
    await forward(20, 50) 
    await backward(40, 100)
    import sys
    sys.exit()
    '''return
    await backward(20, 100)
    await turnRight(35)
    await frontLeft(2*360, 100)
    await forward(35, 50)
    await frontRight(360, 100)
    await turnRight(35)
    await forward(6, 50)
    await frontRight(4*360, 100)
    await backward(10, 100)
    await frontRight(360, 100)
    await turnLeft(60)
    await backward(70, 100)'''
    
    

async def food():
    await frontLeft(45, 100)

if __name__ == "__main__":
    runloop.run(run_grey())
    # runloop.run(food())
    import sys
    sys.exit()