# This program checks the user's choice and the number of items using nested if-else statements.

# Step 1: Set hardcoded values for user choice and number of items
user_choice = 2  # The user has selected option 2
num_items = 5    # The number of items is set to 5

# Step 2: Use if-else to check the user's choice
if user_choice == 1:
    # If the user_choice is 1, print this message
    print('user_choice is 1')
elif user_choice == 2:
    # If the user_choice is 2, check the value of num_items using another if-else (nested inside the previous one)
    if num_items < 0:
        # If num_items is less than 0, print this message
        print('user_choice is 2 and num_items < 0. (nested if statement)')
    else:
        # If num_items is 0 or greater, print this message
        print('user_choice is 2 and num_items >= 0 (nested else statement)')
else:
    # If the user_choice is neither 1 nor 2, print this message
    print('user_choice is neither 1 or 2')
