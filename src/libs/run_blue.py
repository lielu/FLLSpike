import runloop
from drive import *
from attachment import *

from hub import port

async def main():
    await forward(10, 50)
    await frontRight(-720, 100)

if __name__ == "__main__":
    runloop.run(main())
    import sys
    sys.exit()