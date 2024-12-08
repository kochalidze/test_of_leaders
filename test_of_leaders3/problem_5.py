# N5 

#  Write a function to check if two strings are anagrams (contain the same characters in the same frequency).

def anagras(string1, string2):

    return sorted(string1.lower()) == sorted(string2.lower())


print(anagras("listen", "silent"))


# შევქმენი ფუნქცია სადაც გადავეცი ორი სტრინგი, შემდეგ დავწერე კოდი: თუ პირველი სტრინგის სიგრძე არ უდრის მეორე სტრინგის სიგრძეს
#   მაშინ დააბრუნოს False, სხვა შემთხვევაში დააბრუნოს True. შემდეგ ვიხძახებ ფუნქციას