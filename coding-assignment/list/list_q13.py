# Write a Python function that returns the index of a given value in the list.
def find_index(lst, value):
    try:
        return lst.index(value)
    except ValueError:
        return -1
