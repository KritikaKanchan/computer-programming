#Write a function to merge two lists and remove duplicates.
def merge_lists(list1, list2):
    return list(set(list1 + list2))
print(merge_lists([1, 2, 3], [3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
