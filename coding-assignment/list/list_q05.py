# Write a Python function that returns the second largest number in a list.
def second_largest(lst):
    lst = list(set(lst))
    lst.sort()
    return lst[-2]
