#String Length Without Using len()
def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count

print(string_length("hello"))  # Output: 5