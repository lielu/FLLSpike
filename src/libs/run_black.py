import runloop
from drive import *

from hub import port

# Shouldn't be used. Use run_grey instead.

async def main():
    await forward(10, 50)

if __name__ == "__main__":
    runloop.run(main())
    import sys
    sys.exit()