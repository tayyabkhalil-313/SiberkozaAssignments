# A List is a collection which is ordered and changeable. Allows duplicate members.
numbers_tk = [1, 2, 3, 4, 6]
fruits_tk = ['Apples', 'Oranges', 'Grapes', 'Bananna']

# Use a constructor
numbers2_tk = list((1, 2, 3, 4, 5))

# Get a value
print(fruits_tk[1])

# Get the last value
print(fruits_tk[-1])



# Get length
print(len(fruits_tk))

# Append to list
fruits_tk.append('Mangos')

# Remove from list
fruits_tk.remove('Grapes')

# Insert into position
fruits_tk.insert(2, 'Strawberries')

# Change value
fruits_tk[0] = 'Blueberries'

# Remove with pop
fruits_tk.pop(2)

# Reverse list
fruits_tk.reverse()

# Sort list
fruits_tk.sort()

# Reverse sort
fruits_tk.sort(reverse=True)

print(fruits_tk)
