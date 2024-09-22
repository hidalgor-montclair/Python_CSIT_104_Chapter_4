# This program detects ranges of numbers explicitly and implicitly

# Step 1: Explicitly Defined Ranges
x = int(input("Enter a number for explicit check: "))  # The user inputs a number for the explicit range check

# Explicit check using AND operator for ranges
if (x < 0):
    print(f"{x} is a negative number.")  # If x is less than 0, it's a negative number
elif (x >= 0) and (x <= 10):
    print(f"{x} is between 0 and 10.")  # If x is between 0 and 10, inclusive
elif (x >= 11) and (x <= 20):
    print(f"{x} is between 11 and 20.")  # If x is between 11 and 20, inclusive
else:
    print(f"{x} is greater than 20.")  # If x is greater than 20

print()  # Print a blank line for spacing

# Step 2: Implicitly Defined Ranges
x = int(input("Enter a number for implicit check: "))  # The user inputs a number for the implicit range check

# Implicit check without the AND operator for ranges
if (x < 0):
    print(f"{x} is a negative number.")  # If x is less than 0, it's a negative number
elif (x <= 10):
    print(f"{x} is between 0 and 10.")  # If x is between 0 and 10, since the previous condition ruled out x < 0
elif (x <= 20):
    print(f"{x} is between 11 and 20.")  # If x is between 11 and 20, since the previous condition ruled out x <= 10
else:
    print(f"{x} is greater than 20.")  # If x is greater than 20
