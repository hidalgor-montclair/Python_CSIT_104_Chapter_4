# This program prints messages based on a person's age using multiple "if" statements.

# Step 1: Set the age of the user
user_age = int(input("please type your age: "))  # We have hardcoded the age to 26. This could be replaced with user input.

# Note: Each of these "if" statements is separate. More than one message can be printed.
# Step 2: Check different age conditions

if user_age < 16:
    # If the user is younger than 16, print this message
    print('Enjoy your early years.')  # This will not be printed for age 26

if user_age > 15:
    # If the user is older than 15, they can drive
    print('You are old enough to drive.')  # This will be printed for age 26

if user_age > 17:
    # If the user is older than 17, they can vote
    print('You are old enough to vote.')  # This will be printed for age 26

if user_age > 24:
    # If the user is older than 24, most car rental companies will rent to them
    print('Most car rental companies will rent to you.')  # This will be printed for age 26

if user_age > 34:
    # If the user is older than 34, they can run for president
    print('You can run for president.')  # This will not be printed for age 26
