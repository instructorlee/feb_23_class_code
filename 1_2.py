some_string = "some string"

# Lists / arrays

shopping_list = ['marshmallows', 'chocoloate', 'crackers'] # multidimensional array

print ( shopping_list[ 2 ] )

shopping_list.append('wood')

print( shopping_list[ 3 ] )

# del(shopping_list[ 2 ])

print( shopping_list )

shopping_list[ 2 ] = 'lighter fluid'

print( shopping_list.remove('marshmallows') )

"""
    FOR LOOP
"""
"""
for index in range( 10 ): 
    print ( index )


for index in range( 2, 10 ): 
    print ( index )


for index in range( 2, 10, 3 ): 
    print ( index )
print ( '----------------------')

print ( "backwards" )
for index in range( 10, 2, -1 ): 
    print ( index )

completed = [True, False, False]

for index in range(len(shopping_list)):
    print ( shopping_list[ index ], completed[ index ] )
"""


# While loop
x = 1
"""
while ( x <= 10 ):

    print ( x )

    x = x + 1

print("Done")
"""

# is_full = False
max_strength = 5 
strength = 0

while ( strength != max_strength ):
    
    print("Eating!")
    strength += 1

print ("Finished Eating")
