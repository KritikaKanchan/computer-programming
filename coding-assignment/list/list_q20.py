# Write a Python function that returns the elements that are in the first list but not in the second.
def difference_between_lists(lst1, lst2):
    return list(set(lst1) - set(lst2))
