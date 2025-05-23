# 8)

# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

# NOTE: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

# Examples:
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4 of Fo1r people g3ood th5e the2"  -->  "Fo1r the2 g3ood 4 of th5e people"
# ""  -->  ""

def order(n):
    if not n:
        return ""
    
    words = n.split()
    sorted_words = sorted(words,  key=lambda w: int(''.join(filter(str.isdigit, w))))

    return ' '.join(sorted_words)

print(order("is2 Thi1s T4est 3a"))
print(order("4 of Fo1r people g3ood th5e the2"))
print(order(""))