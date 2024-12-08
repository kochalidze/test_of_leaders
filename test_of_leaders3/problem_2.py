# N2

# Create a function that takes a list of numbers, including fractions,
#  and returns the sum of all positive numbers, floored to the nearest integer.


import math
def numbers(lst):
    return sum([math.floor(i) for i in lst if i > 0])

print(numbers([1, -4, 7, 12]))
print(numbers([-1.5, 2.7, -3.3, 4.8]))
print(numbers([]))
print(numbers(([-1, -2, -3])))

# შევქმენი ფუნქცია სახელად numbers, და გადავეცი მას სიას, შემდეგ შევქმენი ცვლადი სადაც შევინახე 0, შემდეგ გადავუარე
#    for loop-ით სიას და ავწერეთ პირობა რომ თუ საიტერაციო ცვლადი მეტია ნულზე მაშინ ზემოთ შექმნილ ცვლადს დაემატოს საიტეტრაციო ცვლადი რომელიც არის გადაქცეული ინტეჯერად
#     საბოლოოდ კი დავაბრუნე num