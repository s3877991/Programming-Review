# TUTORIAL WEEK 11: Putting things together.

# EXERCISE 1:
res = []                            # initial result list
for number in range(1000, 3001):
    string = str(number)            # convert an integer into a string
    # if all digits in an integer are even numbers the numbers meeting the constraint will be printed
    # in a comma-separated sequence on a single line.
    if int(string[0]) % 2 == 0 and int(string[1]) % 2 == 0 and int(string[2]) % 2 == 0 and int(string[3]) % 2 == 0:
        res.append(string)
print(','.join(res))


# EXERCISE 2:
# Way 1: Use for loop
def factorial_iteration(n):
    """Compute factorial of an integer n using iteration"""
    res = 1                         # initial value
    for i in range(1, n + 1):
        res = res * i
    return res                      # final value


print(factorial_iteration(4))


# Way 2: Use recursion
def factorial_recursion(n):
    """
    compute factorial of an integer n using recursion
    """
    if n == 1:                                          # base part
        return 1
    return n * factorial_recursion(n - 1)               # recursion part


print(factorial_recursion(4))


# EXERCISE 3:



# EXERCISE 6:
def is_password_strong_enough(password):
    character_string = '!@#$%^&*'
    upper_case_valid = False
    lower_case_valid = False
    number_valid = False
    character_valid = False
    if 6 <= len(password) <= 12:                        # Check the length of password
        # Check all characters in a password:
        # at least 1 upper-case letter, 1 lower-case letter, 1 number and 1 special character
        for char in password:
            if char.isupper():
                upper_case_valid = True
            elif char.islower():
                lower_case_valid = True
            elif char.isdigit():
                number_valid = True
            elif char in character_string:
                character_valid = True
        return upper_case_valid and lower_case_valid and number_valid and character_valid
    return False


print(is_password_strong_enough('Aa12!@'))
print(is_password_strong_enough('ABC123'))
print(is_password_strong_enough('ABC123abc'))
print(is_password_strong_enough('ABC123abc!@#'))
