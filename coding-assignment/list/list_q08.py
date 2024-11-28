# Write a Python function that finds the intersection (common elements) of multiple lists.
def intersection_of_lists(*lists):
    return list(set(lists[0]).intersection(*lists[1:]))
