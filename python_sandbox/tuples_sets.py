# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# # Simple Tuple 
# fruit_tuple = ('Apple', 'Orange', 'Mango')

# # Using constructure
# fruit_tuple = tuple(('Apple', 'Orange', 'Mango'))

# # Can not change value
# # fruit_tuple[1] = 'Grape'

# # Tuples with one value should have trailing comma
# fruit_tuple_2 = ('Apple', )

# # Get the length of the tuple
# print(len(fruit_tuple_2))

# # Delete the tuple
# del fruit_tuple_2

# print(fruit_tuple)

# A Set is a collection which is unordered and unindexed. No duplicate members.

fruit_set = {'Apple', 'Orange', 'Mango'}

# Check if in set
print('Apple' in fruit_set)

# Add to set
fruit_set.add('Grape')

# Remove from set
fruit_set.remove('Grape')

# Clear Set
fruit_set.clear()

# Delete Set
del fruit_set
