# Write a Python function that removes all whitespace from a string.
def remove_whitespace(s):
    return ''.join(s.split())
s = input()
print(remove_whitespace(s))
