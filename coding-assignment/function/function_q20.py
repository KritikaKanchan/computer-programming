#Write a function that returns the longest word in a list of strings.
def longest_word(words):
    return max(words, key=len)

print(longest_word(["apple", "banana", "cherry", "date"]))  # Output: "banana"
