# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
# numbers = [1, 2, 3, 4, 5]
# Using a constructor
numbers = list((1, 2, 3, 4, 5))
fruits = ['Apples', 'Organges', 'Grapes', 'Pears']

print('Fruit at index 1 ')
print(fruits[1])

# Get len
print('Length of fruits: ')
print(len(fruits))

# Append to a list - This is like the .push method in JS
print('Adding Mango to fruites: ')
fruits.append('Mango')
print(fruits)

# Remove from list
print('Removing Grapes from fruits: ')
fruits.remove('Grapes')
print(fruits)

# Insert into position
print('Adding Strawberries into fruits at index 2: ')
fruits.insert(2, 'Strawberries')
print(fruits)

# Remove from position
print('Removing Pears from index 3')
fruits.pop(3)
print(fruits)

# Reverse list
print('Reversing list')
fruits.reverse()
print(fruits)

# Sort List
print('Sorting list')
fruits.sort()
print(fruits)

# Reverse Sort List
print('Sorting list in Reverse')
fruits.sort(reverse=True)
print(fruits)


# Reverse using for loop