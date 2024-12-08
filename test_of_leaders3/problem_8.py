# N8

#  Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

def longers(nums):

    # if not nums:
    #     return 0
    
    num = set(nums)
    max_len = 0

    if not nums:
        return 0
    
    for i in num:
        if i - 1 not in num:
            num1 = i
            num2 = 1
            while num1 + 1 in num:
                num1 += 1
                num2 += 1
            max_len = max(max_len, num2)

    return max_len


print(longers([9, 1, 4, 7, 3, 2, 8, 5, 6]))


# ახსნა ვერ მოვასწარი