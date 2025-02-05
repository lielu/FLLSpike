from hub import port
import color_sensor
import color
import runloop

from drive import *

# Initialize color sensor
# color_sensor.color(port.A)

class MyColor:
    GREY = 16383
    pass

from hub import light_matrix
def ready(color_detected = "K"):
    light_matrix.write(color_detected)

def detect_color():
    # # Get RGBI values from color sensor
    # r, g, b, i = color_sensor.rgbi(port.B)
    # # Check if values are roughly equal and in mid-range for grey
    # if abs(r - g) <= 40 and abs(g - b) <= 40 and abs(r - b) <= 40:
    #     if 70 <= r <= 150 and 125 <= g <= 150 and 125 <= b <= 150:
    #         return MyColor.GREY

    return color_sensor.color(port.B)

async def detect_color_and_run():

    # Detect color
    detected_color = detect_color()

    # Call corresponding sub run based on detected color.
    # Import sub run modules after color is detected.
    if detected_color is color.RED:
        print("RED")
        from run_red import run_red
        ready("RED")
        await run_red()
    elif detected_color == color.BLUE:
        print("blue")
        from run_blue import run_blue
        ready("blue")
        await run_blue()
    elif detected_color == color.GREEN:
        print("green")
        from run_green import run_green
        ready("green")
        await run_green()
    elif detected_color == color.YELLOW:
        print("YELLOW")
        from run_yellow import run_yellow
        ready("YELLOW")
        await run_yellow()
    elif detected_color == color.BLACK:
        print("BLACK or GREY") # but it should be GREY
        from run_grey import run_grey
        ready("GREY")
        await run_grey()
        # from run_black import run_black
        # await run_black()
    elif detected_color == color.ORANGE:
        print("ORANGE")
        from run_orange import run_orange
        ready("ORANGE")
        await run_orange()
    elif detected_color == color.PURPLE:
        print("PURPLE")
        from run_violet import run_violet
        ready("PURPLE")
        await run_violet()
    elif detected_color == color.WHITE:
        print("WHITE")
        from run_white import run_white
        ready("WHITE")
        await run_white()
    else:
        pass
 
    
    # elif detected_color == MyColor.GREY:
    #     print("GREY")
    #     # await run_grey()

# Run the main detection and execution loop
if __name__ == "__main__":
    runloop.run(detect_color_and_run())
    import sys
    sys.exit(0)
