# Conditional Expression Example
# This program will demonstrate two ways to write an if-else statement
# We'll check if a number is even or odd

# Step 1: Use a traditional if-else statement
number = 10  # We are checking this number

if number % 2 == 0:
    # If the remainder when dividing the number by 2 is 0, the number is even
    even_or_odd = "even"
else:
    # Otherwise, the number is odd
    even_or_odd = "odd"

print(f'Traditional if-else: The number {number} is {even_or_odd}')

# Step 2: Use a conditional expression (ternary operator) to do the same thing in one line
# Conditional expressions work like: variable = expr1 if condition else expr2
even_or_odd_conditional = "even" if number % 2 == 0 else "odd"

# Step 3: Print the result of the conditional expression
print(f'Conditional expression: The number {number} is {even_or_odd_conditional}')
