#Write a function that returns the second largest number in a list.
def second_largest(nums):
    nums = list(set(nums))  # Remove duplicates
    nums.sort()
    return nums[-2] if len(nums) >= 2 else None

print(second_largest([1, 3, 4, 2, 5]))  # Output: 4
