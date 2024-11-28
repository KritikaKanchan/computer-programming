# Write a Python function that checks whether two strings are anagrams (contain the same characters in any order).
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)
