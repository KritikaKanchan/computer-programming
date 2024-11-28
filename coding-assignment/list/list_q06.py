# Write a Python function that takes two lists and returns a new list with the common elements.
def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))
