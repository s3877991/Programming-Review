# TUTORIAL WEEK 11: Putting things together.

# EXERCISE 1:
def even_number_digit(first_number, last_number):
    res = []                                                # initial result list
    for number in range(first_number, last_number + 1):
        string = str(number)                                # convert an integer into a string
        # if all digits in an integer are even numbers the numbers meeting the constraint will be printed
        # in a comma-separated sequence on a single line.
        if int(string[0]) % 2 == 0 and int(string[1]) % 2 == 0 and int(string[2]) % 2 == 0 and int(string[3]) % 2 == 0:
            res.append(string)
    return ', '.join(res)


print(even_number_digit(1000, 3000))        # OUTPUT: 2000, 2002, 2004,... 2884, 2886, 2888


# EXERCISE 2:
# Way 1: Use for loop
def factorial_iteration(n):
    """Compute factorial of an integer n using iteration"""
    res = 1                                                 # initial value
    for i in range(1, n + 1):
        res = res * i
    return res                                              # final value


print(factorial_iteration(4))       # OUTPUT: 24


# Way 2: Use recursion
def factorial_recursion(n):
    """Compute factorial of an integer n using recursion"""
    if n == 1:                                              # base part
        return 1
    return n * factorial_recursion(n - 1)                   # recursion part


print(factorial_recursion(4))       # OUTPUT: 24


# EXERCISE 3:
def substitution_cipher(message, key_to_encrypt):
    """From the plain message and key, encrypt that message with that key"""
    alphabet_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'          # create a string of original alphabet
    encrypted_message = ''                                  # initial result of the encrypted message string
    alphabet_list = list(alphabet_string)                   # convert two character strings into two separate list
    key_list = list(key_to_encrypt)
    encrypt = {}                                            # from those two list, create a dictionary by using
    for key in alphabet_list:                               # Naive methods
        for value in key_list:                              # key: original alphabet letters
            encrypt[key] = value                            # value: encrypted alphabet letter
            key_list.remove(value)
            break
    for char in message:                                    # from a plain message string and the dictionary created
        if char not in alphabet_string:                     # recently, encrypted that message and return the
            encrypted_message += char                       # encrypted one
        else:
            encrypted_message += encrypt[char]
    return encrypted_message


print(substitution_cipher('HELLO WORLD', 'QTGABCDEFHIJKLMNOPRSUVXYZ'))      # OUTPUT: EBJJM XMPJA


# EXERCISE 4:



# EXERCISE 6:
def is_password_strong_enough(password):
    """If password meets some certain requirements, the function returns True. Otherwise, it returns False"""
    character_string = '!@#$%^&*'
    upper_case_valid = False
    lower_case_valid = False
    number_valid = False
    character_valid = False
    if 6 <= len(password) <= 12:                            # Check the length of password
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


print(is_password_strong_enough('Aa12!@'))                  # OUTPUT: True
print(is_password_strong_enough('ABC123'))                  # OUTPUT: False
print(is_password_strong_enough('ABC123abc'))               # OUTPUT: False
print(is_password_strong_enough('ABC123abc!@#'))            # OUTPUT: True
