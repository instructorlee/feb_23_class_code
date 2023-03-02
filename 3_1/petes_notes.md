What tables will we need?
    - what columns?
What types of data will we be working with?
Order to build tables?
Relationships?

Tables:

users -
    - first name 
    - last name ( VARCHAR(40) )
    - email ( VARCHAR(256) )
    - address
    - city
    - state ( CHAR(2) )
    - password
    - fav_pizza_id

pizzas -
    - crust ( INT )
    - size  ( INT )
    - price ( float / decimal )

topings - 
    - name

orders -
    - method ( carryout etc... )
    - order

Relationships:

users / orders one-to-many
orders / pizzas one-to-many 
pizzas / toppings many-to-many
