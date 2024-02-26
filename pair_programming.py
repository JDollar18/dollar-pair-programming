### Task 1 - Feet and Inches to Meters

def feet_and_inches_to_meters(feet, inches):
    inches += feet * 12.0  # converts feet to inches
    meters = inches * 0.0254  # converts inches to meters
    return meters
#good format and documentation

def test_feet_and_inches_to_meters():
    assert feet_and_inches_to_meters(1, 2) = 0.3556
    assert feet_and_inches_to_meters(6, 3) = 1.905
    return "Tests Passed"
