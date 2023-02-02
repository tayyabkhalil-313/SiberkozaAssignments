# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits_tk = ('Apples', 'Oranges', 'Grapes')

# Using a constructor
# fruits2_tk = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2_tk = ('Apples',)

# Get value
print(fruits_tk[1])

# Can't change value
#fruits_tk[0] = 'Pears'

# Delete tuple
del fruits2_tk

# Get length
print(len(fruits_tk))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set_tk = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set_tk)

# Add to set
fruits_set_tk.add('Grape')

# Remove from set
fruits_set_tk.remove('Grape')

# Add duplicate
fruits_set_tk.add('Apples')

# Clear set
fruits_set_tk.clear()

# Delete
del fruits_set_tk

#print(fruits_set_tk)