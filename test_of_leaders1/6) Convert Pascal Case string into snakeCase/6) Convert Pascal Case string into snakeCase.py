# 6)
# You will receive a string which will contain words in PascalCase, your job is to convert them into snake_case.

# Examples:
# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7 Test"        -->  "app7_test"
# 1                 -->  "1"

import re

def pascal_to_snake(s):

    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower().replace(' ', '_')
    return snake_case

print(pascal_to_snake("TestController"))
print(pascal_to_snake("MoviesAndBooks"))
print(pascal_to_snake("App7 Test"))
print(pascal_to_snake("1"))