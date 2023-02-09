print ( "Hello World!" )

# variables
name = "fred flintstone" # string
age = 5 # number ( integer )
likes_chocolate = True # boolean

print ( name )

print ( name.title() )
print ( name.count('f') )

name = name.title()

print ( name + " is ", age, " years old." )
#print ( name + " is " + age + " years old." )

print ( name + " is " + str(age) + " years old." ) # type casting

# print ( f'{name} is {age} years old.' )

# IF Statements

if 1 == 2:
    print ( "true" )

likes_chocolate = False
if likes_chocolate:
    print ("Likes chocolate")

else:
    print("Doesn't like chocolate.")

count = 0

if count:
    print( "more than 0")

else:
    print("count is 0")

# ternary operator
print ( "like" if likes_chocolate else "does not like" )

print ( 1 + 1 )

print ( f'{name} is {age} years old. And I {"like" if likes_chocolate else "do not like"} chocolate.' )

if age <= 12:
    pass

elif age <= 19:
    print ( f"{name} is a teenager." )

else:
    print ( f"{name} is a adult." )


speed = 17
vehicle_type = 'emergency'
light_color = 'yellow'

if speed > 0:
    if light_color == "white" and vehicle_type != "public":

        if vehicle_type == "emergency" and speed > 30:
            speed = 30
        else:
            speed = 0

    elif light_color == "green" and vehicle_type == "public":
        speed = 0

    elif light_color == "yellow":
        if vehicle_type == "human" or vehicle_type == "public":
            speed = 0
        elif vehicle_type == "emergency" and speed > 30:
            speed = 30
        else:
            speed = 20

    elif light_color == "red":
        if vehicle_type == "emergency":
            speed = 20
        else:
            speed = 0

print ( f'The speed is: {speed}' )