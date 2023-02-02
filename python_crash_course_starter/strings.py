# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name_tk = 'Harry'
age_tk = 31

print('My name is ' + name_tk + ' and I am ' + str(age_tk))
# String Formatting
print(f'My name is {name_tk} and I am {age_tk}')
# String Methods

s_tk = 'Hello World!'

# Capitalize string
print(s_tk.capitalize())

# Make all uppercase
print(s_tk.upper())

# Make all lower
print(s_tk.lower())

# Swap case
print(s_tk.swapcase())

# Get length
print(len(s_tk))

# Replace
print(s_tk.replace('World', 'Everyone'))

# Count
sub = 'h'
print(s_tk.count(sub))

# Starts with
print(s_tk.startswith('Hello'))

# Ends with
print(s_tk.endswith('!'))

# Split into a list
print(s_tk.split())

# Find position
print(s_tk.find('r'))

# Is all alphanumeric
print(s_tk.isalnum())

# Is all alphabetic
print(s_tk.isalpha())

# Is all numeric
print(s_tk.isnumeric())
