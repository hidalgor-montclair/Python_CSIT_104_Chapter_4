# Identity Operators Example: is / is not

# Step 1: Assign values to variables
w = 500  # w is assigned the value 500
x = 500 + 500  # x is assigned the result of 500 + 500, which is 1000
y = w + w  # y is also assigned the value 1000, calculated from w + w
z = x  # z is assigned the same object as x (they are bound to the same object)

# Step 2: Check if z and x are the same object
# The 'is' operator checks if two variables reference the same object in memory
if z is x:  
    print('z and x are bound to the same object')  # This will be True because z is assigned to x

# Step 3: Check if z and y are NOT the same object
# The 'is not' operator checks if two variables reference different objects in memory
if z is not y:
    print('z and y are NOT bound to the same object')  # This will be True because z is not the same object as y

# Now let's compare using the equality operator '=='
# Step 4: Check if z and y have the same value
# The '==' operator checks if two variables have the same value, even if they are different objects
if z == y:
    print('z and y have the same value')  # This will be True because both z and y have the value 1000

# Step 5: Check if z and x have the same value
# Since z and x are the same object, they obviously have the same value too
if z == x:
    print('z and x have the same value')  # This will also be True, as z is referencing x
