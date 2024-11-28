# Write a Python function that reverses the words in a string but keeps the characters in each word intact.
def reverse_words(s):
    words = s.split()
    return ' '.join(reversed(words))
