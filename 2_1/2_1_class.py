print ('-----------------------')
person = {
    'first_name': 'Jessie', 
    'lottery_nums': [2, 9, 14, 50, 55]
    }

print( person['lottery_nums'][0] )

print ('-----------------------')

print( person['lottery_nums'][4] )

print ('-----------------------')

for number in person['lottery_nums']:
    print(
        'x' if number % 2 != 0 else number
    )

print ('-----------------------')

print( person['lottery_nums'][1] )


print ('-----------------------')

def add_nums(num_1, num_2):
    print( num_1 + num_2 )

add_nums(3, 5)

print ('-----------------------')

add_nums(6, int('5'))

# What information should you provide when reaching out for help?


print ('-----------------------')

def make_character(name, age, is_magical=False, can_fly=False):
    return {
        'name': name,
        'age': age,
        'is_magical': is_magical,
        'can_fly': can_fly
    }

print(make_character('Fred', 35))

print ('-----------------------')

make_character('Fred')

make_character('Fred', 35, can_fly=True)

print ('-----------------------')

# Why is this complaining
make_character('Fred', 35, can_fly=True)

make_character('Fred', can_fly=True, age=35)