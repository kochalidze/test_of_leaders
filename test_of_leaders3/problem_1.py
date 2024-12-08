# N1



# Create a function that takes a list of numbers and returns the sum of all positive numbers.

def numbers(numbers_list):

    num = 0 
    for i in numbers_list:
        if i > 0:
            num += i
        
    return num

print(numbers([-1, -2, -3, -4]))
print(numbers([1, -4, 7, 12]))
print(numbers([]))

# შევქმენი ფუნქცია სახელად numbers, და გადავეცი მას სიას, შემდეგ შევქმენი ცვლადი სადაც შევინახე 0, შემდეგ გადავუარე
#    for loop-ით სიას და ავწერეთ პირობა რომ თუ საიტერაციო ცვლადი მეტია ნულზე მაშინ ზემოთ შექმნილ ნულს დაემატოს საიტეტრაციო ცვლადი
#     საბოლოოდ კი დავაბრუნე num