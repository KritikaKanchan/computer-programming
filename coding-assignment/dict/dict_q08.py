# Define a function 'test' that updates the list values within a dictionary.
def test(dictionary):
    dictionary['Math'] = [x + 1 for x in dictionary['Math']]
    dictionary['Physics'] = [x - 2 for x in dictionary['Physics']]
    dictionary['Chemistry'] = [x + 3 for x in dictionary['Chemistry']]
    return dictionary

# Create a dictionary 'dictionary' with keys 'Math', 'Physics', and 'Chemistry', and lists as values.
dictionary = { 
    'Math': [88, 89, 90], 
    'Physics': [92, 94, 89],
    'Chemistry': [90, 87, 93]
}

print("Original Dictionary:")
print(dictionary)

print("Update the list values of the said dictionary:")

print(test(dictionary))
