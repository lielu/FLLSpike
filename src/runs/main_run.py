from hub import port
import color_sensor
import color
import runloop

from drive import *

# Import sub run modules
from run_red import run_red
from run_blue import run_blue
from run_green import run_green
from run_yellow import run_yellow
from run_black import run_black
from run_grey import run_grey
from run_orange import run_orange
from run_violet import run_violet

# Initialize color sensor
# color_sensor.color(port.A)

def detect_color():
    # Get RGBI values from color sensor
    r, g, b, i = color_sensor.rgbi(port.B)
    # Check if values are roughly equal and in mid-range for grey
    if abs(r - g) <= 30 and abs(g - b) <= 30 and abs(r - b) <= 30:
        if 70 <= r <= 150 and 70 <= g <= 150 and 70 <= b <= 150:
            return color.GREY

    return color_sensor.color(port.B)

async def detect_color_and_run():
    # forward(20, 50)

    # Detect color
    detected_color = detect_color()

    # Call corresponding sub run based on detected color
    if detected_color is color.RED:
        # print("red")
        await run_red()
    elif detected_color == color.BLUE:
        # print("blue")
        await run_blue()
    elif detected_color == color.GREEN:
        # print("green")
        await run_green()
    elif detected_color == color.YELLOW:
        # print("YELLOW")
        await run_yellow()
    elif detected_color == color.BLACK:
        print("BLACK")
        # await run_black()
    elif detected_color == color.GREY:
        print("GREY")
        # await run_grey()

# Run the main detection and execution loop
runloop.run(detect_color_and_run())
import sys
sys.exit(0)
