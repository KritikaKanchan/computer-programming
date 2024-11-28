#Write a function that accepts a list of integers and returns the product of all numbers.
def product_of_numbers(nums):
    product = 1
    for num in nums:
        product *= num
    return product

print(product_of_numbers([1, 2, 3, 4]))  # Output: 24
