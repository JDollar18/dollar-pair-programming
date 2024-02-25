### Task 1 - Feet and Inches to Meters

def feet_and_inches_to_meters(feet, inches):
    inches += feet * 12.0  # converts feet to inches
    meters = inches * 0.0254  # converts inches to meters
    return meters