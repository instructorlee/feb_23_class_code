"""
    Challenge 1
            
    Parameters
        - values will be 1 or 2
        - the same value may be given consecutively
        - there will always be a wall on either side ( outter walls )

    Tests
        - Pass all given tests
        - Add 2 tests of your own that fit the above parameters
"""

def count_water_units(terraces):
    
    units = 0

    for element in terraces:
        if int(element) == 1:
            units += 1

    return units

# tests
print (f"test 1.1: {'good' if count_water_units('212') == 1 else 'failed'}")
print (f"test 1.2: {'good' if count_water_units('2122112') == 3 else 'failed'}")