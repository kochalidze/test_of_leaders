# N6

#  Write a function to find the common elements between two lists.

def elements(list1, list2):

    set1 = set(list1)
    set2 = set(list2)

    return list(set1.intersection(set2))

print(elements([1, 2, 3], [2, 3, 4]))