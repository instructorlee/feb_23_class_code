e_list = ['a', 'b', 'c']
e_tuple = ('1', '2', '3')

for element in e_list:
    print(element)

for element in e_tuple:
    print(element)

e_list.append('d')
e_list[1] = 'x'
e_tuple[1] = 'x'

some_string = """
    This just created some space in memory. 
    A pointer called 'some_string' tells where it is in memory.
    """

some_string += """ 
    Now a new place in memory is filled with the updated string and the pointer, 
    'some_string' is updated to point to the new location.
    """

some_string += """
    Now a new place in memory is filled with the updated string and the pointer, 
    'some_string' is updated to point to the new location.

    Strings are immutable; they are not updated in memory. 
    Instead, new memory is used to hold the updated value.
    Some other immutable types are: int, tuple, boolean.

    """

# garbage collection

# mutable objects
some_list = [True, False, True, False]
some_list[1] = None

# Dictionary
some_dict = {
    'name': "Fred Flintstone",
    'age': 35
}

some_dict['age'] = 34

"""
    Mutable objects allow the values to be updated in-place in memory
        - requires more overhead to manage the data

    tuples use immutability to improve speed
        - reduced functionality means less overhead
"""

