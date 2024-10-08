def straight(motor, speed, distance=None, degrees=None, seconds=None):
    """
    Control a drive motor for FLL Spike.
    
    Args:
        motor: The motor object to control.
        speed (int): The speed of the motor (-100 to 100).
        distance (float, optional): The distance to travel in centimeters.
        degrees (int, optional): The number of degrees to rotate the motor.
        seconds (float, optional): The number of seconds to run the motor.
    """
    if distance is not None:
        # Assuming a standard wheel diameter of 5.6 cm for LEGO wheels
        # Circumference = pi * diameter
        wheel_circumference = 3.14159 * 5.6
        # Calculate degrees to rotate based on distance
        degrees_to_rotate = (distance / wheel_circumference) * 360
        motor.run_for_degrees(int(degrees_to_rotate), speed)
    elif degrees is not None:
        motor.run_for_degrees(degrees, speed)
    elif seconds is not None:
        motor.run_for_seconds(seconds, speed)
    else:
        motor.start(speed)

    motor.wait_until_not_moving()


