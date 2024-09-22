# This program checks if a number is within a certain range using operator chaining

# Step 1: Ask the user to enter a number
number = int(input("Enter a number between 1 and 100: "))  # The user inputs a number, which is converted to an integer

# Step 2: Use operator chaining to check if the number is between 1 and 100
if 1 <= number <= 100:
    # If the number is between 1 and 100, this message will be printed
    print(f"{number} is within the range of 1 to 100.")
else:
    # If the number is not in the range, this message will be printed
    print(f"{number} is outside the range of 1 to 100.")
