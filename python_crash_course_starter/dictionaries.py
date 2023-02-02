# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
person_tk = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use constructor
# person2_tk = dict(first_name='Sara', last_name='Williams')

# Get value
print(person_tk['first_name'])
print(person_tk.get('last_name'))

# Add key/value
person_tk['phone'] = '555-555-5555'

# Get dict keys
print(person_tk.keys())

# Get dict items
print(person_tk.items())

# Copy dict
person2_tk = person_tk.copy()
person2_tk['city'] = 'Boston'

# Remove item
del(person_tk['age'])
person_tk.pop('phone')

# Clear
person_tk.clear()

# Get length
print(len(person2_tk))

# List of dict
people_tk = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people_tk[1]['name'])