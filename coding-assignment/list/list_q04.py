#Write a function to count the occurrence of a specific element in a list.
def count_occurrences(nums, val):
    return nums.count(val)

nums = [1, 2, 3, 1, 1, 4]
print(count_occurrences(nums, 1))  # Output: 3
