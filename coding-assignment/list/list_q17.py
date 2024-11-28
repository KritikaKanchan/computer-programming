# Write a Python function that finds the first non-repeated element in a list.
def first_non_repeated(lst):
    for item in lst:
        if lst.count(item) == 1:
            return item
    return None
