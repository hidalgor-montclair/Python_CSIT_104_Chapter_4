# This program gives a special message based on how many years someone has been married

# Step 1: Get the number of years married from the user
num_years = int(input("Enter number of years married: "))  # The user enters the number of years, which is converted to an integer

# Step 2: Check the number of years and print a special message for specific anniversaries
if num_years == 1:
    # If they have been married for 1 year, print a message
    print("Your first year -- great!")
elif num_years == 10:
    # If they have been married for 10 years, print a message
    print("A whole decade -- impressive.")
elif num_years == 25:
    # If they have been married for 25 years, print a message
    print("Your silver anniversary -- enjoy.")
elif num_years == 50:
    # If they have been married for 50 years, print a message
    print("Your golden anniversary -- amazing.")
else:
    # If they have been married for a number of years that is not 1, 10, 25, or 50, print a different message
    print("Nothing special.")
