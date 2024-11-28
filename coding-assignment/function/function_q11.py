#Write a function that takes a number and returns its binary representation.
def to_binary(n):
    return bin(n)[2:]

print(to_binary(10))  # Output: "1010"
