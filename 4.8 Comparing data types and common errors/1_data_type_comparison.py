# Step 1: Compare integers
# Numbers are compared arithmetically (like in math)
num1 = 5
num2 = 3
print(f'Is 5 greater than 3? {num1 > num2}')  # True because 5 is greater than 3

# Step 2: Compare floating-point numbers
# Floating-point numbers are tricky because of how they are stored in memory
float1 = 0.1 + 0.2
float2 = 0.3
print(f'Is 0.1 + 0.2 equal to 0.3? {float1 == float2}')  # This is False due to precision issues with floating points!

# Step 3: Compare strings
# Strings are compared by their character's "number value" (ASCII or Unicode)
my_str = 'Tuesday'
your_str = 'tuesday'
print(f'Is "Tuesday" equal to "tuesday"? {my_str == your_str}')  # False because T and t are different in computers

# Step 4: List comparison
# Lists are compared by their elements in order
list1 = [1, 5, 2]
list2 = [1, 4, 3]
print(f'Is [1, 5, 2] less than [1, 4, 3]? {list1 < list2}')  # False because 5 is greater than 4

# Step 5: Tuple comparison
# Like lists, tuples are compared element by element
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
print(f'Is (1, 2, 3) equal to (1, 2, 4)? {tuple1 == tuple2}')  # False because the last elements don't match

# Step 6: Dictionary comparison
# Dictionaries are compared by their keys and values
dict1 = {'name': 'Alice', 'age': 10}
dict2 = {'name': 'Alice', 'age': 10}
print(f'Are the two dictionaries equal? {dict1 == dict2}')  # True because they have the same keys and values

# Step 7: TypeError example
# Trying to compare incompatible types like numbers and strings causes an error
try:
    print(1 < 'abc')  # This will raise a TypeError because you can't compare numbers with strings
except TypeError:
    print('You cannot compare a number with a string!')

# Step 8: Common string comparison mistake
# Strings are case-sensitive, meaning 'A' and 'a' are not equal
str1 = 'Apple'
str2 = 'apple'
print(f'Is "Apple" equal to "apple"? {str1 == str2}')  # False because 'A' is not equal to 'a'
