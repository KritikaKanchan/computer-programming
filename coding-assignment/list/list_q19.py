# Write a Python function that returns the longest string in a list of strings.
def longest_string(lst):
    return max(lst, key=len)
