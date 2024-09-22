# This program checks if a number is even or odd

# Step 1: Get a number from the user
user_num = int(input("Enter a number: "))  # The user enters a number, which is converted to an integer

# Step 2: Find the remainder when the number is divided by 2
div_remainder = user_num % 2  # The remainder when user_num is divided by 2 is stored in div_remainder

# Step 3: Check if the remainder is 0 (which means the number is even)
if div_remainder == 0:
    # If the remainder is 0, the number is even
    print(f"{user_num} is even.")
else:
    # If the remainder is not 0, the number is odd
    print(f"{user_num} is odd.")
