# Step 1: Create a list of famous soccer players in the Barcelona FC roster
barcelona_fc_roster = ['Alves', 'Messi', 'Fabregas']  # List of players on the team

# Step 2: Ask the user to input a name to check on the roster
name = input('Enter name to check: ')  # The user types a name to check if it's on the roster

# Step 3: Use the 'in' operator to check if the name is on the roster
if name in barcelona_fc_roster:
    # If the name is found in the list, print this message
    print(f'Found {name} on the roster.')
else:
    # If the name is NOT found in the list, print this message
    print(f'Could not find {name} on the roster.')

# --- This part demonstrates the 'not in' operator ---

# Step 4: Now, let's reverse the logic using 'not in' to check if the name is NOT on the roster
if name not in barcelona_fc_roster:
    # If the name is NOT found in the list, print this message
    print(f'Could not find {name} on the roster.')
else:
    # If the name is found in the list, print this message
    print(f'Found {name} on the roster.')
