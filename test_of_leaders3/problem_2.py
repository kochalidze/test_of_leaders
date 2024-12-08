# N2

# Create a function that takes a list of numbers, including fractions,
#  and returns the sum of all positive numbers, floored to the nearest integer.


def numbers(numbers_list):

    num = 0
    for i in numbers_list:
        if num > 0:
            num += int(i)
        
    return num

print(numbers([1, -4, 6, 15]))

# შევქმენი ფუნქცია სახელად numbers, და გადავეცი მას სიას, შემდეგ შევქმენი ცვლადი სადაც შევინახე 0, შემდეგ გადავუარე
#    for loop-ით სიას და ავწერეთ პირობა რომ თუ საიტერაციო ცვლადი მეტია ნულზე მაშინ ზემოთ შექმნილ ნულს დაემატოს საიტეტრაციო ცვლადი
#     საბოლოოდ კი დავაბრუნე num