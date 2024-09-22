# This program calculates the insurance price based on the user's age.

# Step 1: Ask the user for their age
user_age = int(input("Enter your age: "))  # The user inputs their age, which is converted to an integer

# Step 2: Check the user's age and set the insurance price
if user_age < 16:
    # If the user is younger than 16, they are too young for insurance
    print("Too young.")
    insurance_price = 0  # No insurance price for someone too young
elif user_age < 25:
    # If the user is between 16 and 24, the insurance price is $4800
    insurance_price = 4800
elif user_age < 40:
    # If the user is between 25 and 39, the insurance price is $2350
    insurance_price = 2350
else:
    # If the user is 40 or older, the insurance price is $2100
    insurance_price = 2100

# Step 3: Output the insurance price
print(f"Annual price: ${insurance_price}")  # Print the final insurance price
