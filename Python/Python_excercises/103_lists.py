# Lists!

# Fine a list with cool things inside!
    # Examples: Christmas list, things you would by with the lottery
    # It must have 5 items
    # Complete the sentence:
    # Lists are organized using: _indexs______?????

example_xmas = ['walkie talkies', 'socks', 'lynx']

# Print the lists and check it's type
print(type(example_xmas))

# Print the list's first object
print(example_xmas[0])

# Print the list's second object
print(example_xmas[1])

# Print the list's last object
print(example_xmas[-1])

# Re-define the first item on the list and
example_xmas[0] = 'Action man'


# Re-define another item on the list and print all the list
example_xmas[1] = 'Barbie'
print(example_xmas)

# Add an item to the list and print the list
example_xmas.append('playstation')
print(example_xmas)
# Remove an item from the list and print the list
example_xmas.pop(-1)
print(example_xmas)

# Add two items to list and print the list
example_xmas.append('iphone')
example_xmas.append('car')
print(example_xmas)
