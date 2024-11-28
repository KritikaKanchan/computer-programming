#Write a function that returns a dictionary of character frequencies in a string.
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

print(char_frequency("hello"))  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}