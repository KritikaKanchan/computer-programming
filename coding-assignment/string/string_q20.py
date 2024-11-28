# Write a Python function that checks if one string is a rotation of another string.
def are_rotations(s1, s2):
    if len(s1) != len(s2):
        return False
    return s1 in (s2 + s2)
