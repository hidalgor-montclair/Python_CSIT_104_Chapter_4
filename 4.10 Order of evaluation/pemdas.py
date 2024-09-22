# PEMDAS Example
# This program will show how math expressions are evaluated in Python
# PEMDAS stands for Parentheses, Exponents, Multiplication, Division, Addition, Subtraction

# Step 1: An expression without parentheses
# Multiplication happens before addition according to PEMDAS
result_without_parentheses = 5 + 3 * 2  
# First, 3 * 2 is calculated (which is 6), then 5 + 6 = 11
print(f'Without parentheses: 5 + 3 * 2 = {result_without_parentheses}')

# Step 2: The same expression but with parentheses
# Parentheses change the order: addition happens before multiplication
result_with_parentheses = (5 + 3) * 2  
# First, 5 + 3 is calculated (which is 8), then 8 * 2 = 16
print(f'With parentheses: (5 + 3) * 2 = {result_with_parentheses}')
