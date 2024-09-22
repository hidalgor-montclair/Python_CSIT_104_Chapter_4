# This program demonstrates how logical operators work in Python

# Step 1: Define variables x and y
x = 7
y = 9

# AND Operator Example
# Explanation: AND returns True only if both conditions are True
print("(x > 0) AND (y < 10):", (x > 0) and (y < 10))  # Both conditions are True, so the result is True

# Another AND Example
# Explanation: If one of the conditions is False, the result is False
print("(x > 0) AND (y < 5):", (x > 0) and (y < 5))  # The second condition is False, so the result is False

# OR Operator Example
# Explanation: OR returns True if at least one condition is True
print("(x < 0) OR (y > 10):", (x < 0) or (y > 10))  # Both conditions are False, so the result is False
print("(x < 0) OR (y > 5):", (x < 0) or (y > 5))  # The second condition is True, so the result is True

# NOT Operator Example
# Explanation: NOT flips the result, so True becomes False and False becomes True
print("NOT (x < 0):", not (x < 0))  # x is not less than 0, so the condition is False, and NOT makes it True
print("NOT (x > 0):", not (x > 0))  # x is greater than 0, so the condition is True, and NOT makes it False
