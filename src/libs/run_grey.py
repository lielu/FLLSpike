import runloop
from attachment import *
from drive import *

from hub import port

async def run_grey():
    await forward(20, 50)
    await test_attachment()

if __name__ == "__main__":
    runloop.run(run_grey())
    import sys
    sys.exit()