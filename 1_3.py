name = 'fred flintstone'
age = 5 

# What's wrong with this line?
#print ( name + " is " + str(age) + " years old." )

# pop or corn?
"""
if 0 == True:
    print ('pop')

else:
    print('corn')
    """

# -----------
"""
price = 31

if price < 10:
    print("A")

elif price > 15 and price < 22:
    print ("B")

elif price < 20:
    print("C")

elif int(price / 2) == 22:
    print("D")

elif price < 30 and price % 2 == 0: # modulus
    print("E")

elif price > 19:
    print("F")

else:
    print('oops')
"""

"""
    objects / Dictionary
"""
"""
simple_object = {
    'key': "value"
}

print ( simple_object['key'] )

shopping_list_item = {
    'name': "milk",
    'completed': False
}

print ( shopping_list_item['name'] )

shopping_list_item['completed'] = True

del(shopping_list_item['completed'])

print ( f"{shopping_list_item['name']} {'has' if shopping_list_item['completed'] else 'has not'} been selected." )

new_shopping_list = [
    {
        "name": "milk",
        "completed": False
    },
    {
        "name": "chocolate",
        "completed": True
    },
    {
        "name": "crackers",
        "completed": False
    }
]

for item in new_shopping_list:
    print ( f"{item['name']} {'has' if item['completed'] else 'has not'} been selected.")
"""
"""
  Functions
    - A code block that does one thing and does it well. ( reusable )
"""

def some_function():
    print ( "Hello World!" )

some_function()

def some_function_with_parameter(name):
    print ( f"Hello {name}!" )

sharper = 'Wilma'
some_function_with_parameter(sharper)

def some_function_with_default_parameter(name, is_admin=False):
    print ( f"{name} is{'' if is_admin else ' not'} admin" )

some_function_with_default_parameter('Fred', True)

def some_function_that_returns_something(value):
    return value + 5

new_value = some_function_that_returns_something(3)
new_value += new_value * .02
print ( f"The new Value is: {new_value}!" )

def some_function_with_multiple_params(value_1, value_2):
    return value_1 + value_2

print ( f"The sum is: {some_function_with_multiple_params(1, 2)}!" )