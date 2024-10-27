# 3)
# Create a program that receives a list and removes duplicate elements while maintaining the original order.
# Examples:
# [1, 2, 2, 3, 4, 4, 5] --> [1, 2, 3, 4, 5]
# ['a', 'b', 'a', 'c'] --> ['a', 'b', 'c']

def remove_duplicates():
    lst =  [1, 2, 2, 3, 4, 4, 5 ]

    list= []
    seen = set()
    for i in lst:
        if i not in seen:
            list.append(i)
            seen.add(i)
    return list

remove_duplicates()