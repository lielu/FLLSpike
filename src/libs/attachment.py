from hub import port
from motor import run_for_degrees
import runloop

async def frontRight(degrees, speed):
    run_for_degrees(port.A, degrees, int(round(speed / 100 * -1050)))

async def frontLeft(degrees, speed):
    run_for_degrees(port.A, degrees, int(round(speed / 100 * 1050)))

async def rearLeft(degrees, speed):
    run_for_degrees(port.F, degrees, int(round(speed / 100 * 1050)))

async def rearRight(degrees, speed):
    run_for_degrees(port.F, degrees, int(round(speed / 100 * -1050)))

async def test_attachment(): #test code for drive functions
    await frontRight(360, 100)
    await frontLeft(360, 100)
    await rearRight(360, 100)
    await rearLeft(360, 100)

if __name__ == "__main__":
    runloop.run(test_attachment())
    import sys #Imports Sys so we can exit code
    sys.exit() #Exits out of code