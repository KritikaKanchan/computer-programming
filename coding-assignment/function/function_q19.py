#Write a function that sorts a list of tuples by the second element in each tuple.
def sort_tuples(lst):
    return sorted(lst, key=lambda x: x[1])

print(sort_tuples([(1, 3), (4, 1), (2, 2)]))  # Output: [(4, 1), (2, 2), (1, 3)]
