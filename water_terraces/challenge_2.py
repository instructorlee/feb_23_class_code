"""
    Challenge 2

    
    Parameters
        - values will be 1 or 2
        - the same value may be given consecutively
        - there will always be a starting wall.
        - there may not be an ending wall.

    Tests
        - Pass all previous tests
        - Pass all new tests
"""

# 2 1 2 1 2 1    /  2 1 2 1 2 1 1 2
def count_water_units(terraces):
    pass

print (f"test 2.1: {'good' if count_water_units('212') == 1 else 'failed'}")
print (f"test 2.2: {'good' if count_water_units('2122112') == 3 else 'failed'}")
print (f"test 2.3: {'good' if count_water_units('212121') == 2 else 'failed'}")
print (f"test 2.4: {'good' if count_water_units('2121211') == 2 else 'failed'}")