# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Andre'
age = 25

# Concatenate
print('Hello, I am ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position
print('{1}, {2}, {0}'.format('a', 'b', 'c'))
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F Strings
print(f'My name is {name} amd I am {age}')

# String Methods
s = 'hello there world';

# Uppercases first letter
print(s.capitalize())

# Makes all upper
print(s.upper())

# Makes all lower
print(s.lower())

# Swaps case
print(s.swapcase())

# Gets length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = "h"
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())


