# Write a Python function that checks if a given list is the same forwards and backwards.
def is_palindrome(lst):
    return lst == lst[::-1]
