# Step 1: Create a dictionary (my_dict) where keys are letters, and values are numbers
my_dict = {'A': 1, 'B': 2, 'C': 3}  # A dictionary with three key-value pairs

# Step 2: Use the 'in' operator to check if a specific key ('B') is in the dictionary
# We are only checking if the key exists, not the value
if 'B' in my_dict:
    # If 'B' is found as a key in the dictionary, print this message
    print("Found 'B'")
else:
    # If 'B' is not found, print this message
    print("'B' not found")

# Step 3: Membership operator does not check the values of the dictionary, only keys
# Now, let's check if the number 3 is a key in the dictionary (which it isn't)
if 3 in my_dict:
    # If 3 is found as a key in the dictionary, print this message
    print("Found 3")
else:
    # If 3 is not found as a key, print this message
    print("3 not found")
