# Write a Python function that finds the first non-repeated character in a string.
def first_non_repeated(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None
