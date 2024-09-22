# This program calculates a hotel rate. If a couple has been married for 50 years, they get a 50% discount.

# Step 1: Set the initial hotel rate
hotel_rate = 150  # The standard hotel rate is $150
print()
# Step 2: Ask the user how many years they have been married
num_years = int(input("Enter years married: "))  # The user inputs the number of years married, which is converted to an integer
print()
# Step 3: Check if the couple has been married for 50 years
if num_years == 50:
    # If the couple has been married for 50 years, they get a discount
    print("Congratulations on 50 years of marriage!")
    hotel_rate = hotel_rate / 2  # The hotel rate is cut in half (50% discount)

# Step 4: Output the hotel rate, formatted to show two decimal places
print(f"Your hotel rate: ${hotel_rate:.2f}")  # The final hotel rate is printed, with two decimal places

print()