# 5)
# Create a program that checks if a given string is a palindrome (reads the same forward and backward). The function should ignore spaces, punctuation, and capitalization.
# Examples:
# "A man a plan a canal Panama" --> True
# "Hello" --> False

import re

def is_palindrome(s):

    cleaned = re.sub(r'[^a-z0-9]', '', s.lower())

    return cleaned == cleaned[::-1]

print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("Hello"))
