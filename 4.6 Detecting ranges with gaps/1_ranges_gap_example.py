# This program checks if an office number is valid based on two valid ranges: 100-150 or 200-250

# Step 1: Get the office number as input from the user
office_num = int(input("Enter the office number: "))  # The user inputs the office number, which is converted to an integer

# Step 2: Check if the office number falls within one of the two valid ranges using `if-elif-else`
# First, we check if the office number is between 100 and 150 (inclusive)
if office_num >= 100 and office_num <= 150:
    print(f"Office number {office_num} is valid.")  # Output for valid office number in range 100-150
# Next, we check if the office number is between 200 and 250 (inclusive)
elif office_num >= 200 and office_num <= 250:
    print(f"Office number {office_num} is valid.")  # Output for valid office number in range 200-250
else:
    # If the office number is not in either range, it's invalid
    print(f"Office number {office_num} is invalid.")  # Output for invalid office number

# Step 3: Output the result using combined conditions in a single branch
# Here, we check if the office number falls within either range using the `or` operator
if (office_num >= 100 and office_num <= 150) or (office_num >= 200 and office_num <= 250):
    print(f"(Using combined condition) Office number {office_num} is valid.")
else:
    print(f"(Using combined condition) Office number {office_num} is invalid.")
