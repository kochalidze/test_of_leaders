# N4

#  Create a function that finds the length of the longest substring without repeating characters.

def length_substring(substring: str) -> int:
    char = set()
    len_max = 0
    start = 0

    for i in range(len(substring)):
        while substring[i] in char:
            char.remove(substring[start])
            start += 1
        char.add(substring[i])
        len_max = max(len_max, i - start + 1)
    
    return len_max

print(length_substring("abcabcbb"))