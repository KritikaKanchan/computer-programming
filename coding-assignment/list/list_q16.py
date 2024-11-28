# Write a Python function that removes all occurrences of a given value from the list.
def remove_value(lst, value):
    return [x for x in lst if x != value]
