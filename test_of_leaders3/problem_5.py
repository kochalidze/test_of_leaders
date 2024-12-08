# N5 

#  Write a function to check if two strings are anagrams (contain the same characters in the same frequency).

def anagras(string1, string2):

    if len(string1) != len(string2):
        return False
    else:
        return True

print(anagras("listen", "silent"))
print(anagras("hello", "world"))