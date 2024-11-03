import runloop
from drive import *


from hub import port

async def main():
    await forward(40, 50)
    await turnRight(90)
    await forward(35, 50)
    await backward(15, 50)
    await turnLeft(80)
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