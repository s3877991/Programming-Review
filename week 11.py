# Exercise 2:
def factorial_iteration(n):
    """Compute factorial of an integer n using interation"""
    res = 1                     # ket qua ban dau
    for i in range(1, n + 1):
        res = res * i
    return res                  # ket qua chinh thuc

print(factorial_iteration(4))


def factorial_recursion(n):
    """
    compute factorial of an integer n using recursion
    """
    if n == 1:                  # phan goc
        return 1
    return n * factorial_recursion(n - 1)       # phan de quy

print(factorial_recursion(4))


# Exercise 6:
def is_password_strong_enough(password):
    """
    return a Boolean value True if the provided password is strong enough
    False otherwise
    """
    # kiem tra do dai mat khau
    lower_case_valid = False
    digit_valid = False
    if len(password) >= 6 and len(password) <= 12:
        for char in password:
            if char.islower():
                lower_case_valid = True
            elif char.isdigit():
                digit_valid = True
        return lower_case_valid and digit_valid
    else:
        return False

print(is_password_strong_enough('ABC123'))
print(is_password_strong_enough('aaaBBB'))
print(is_password_strong_enough('ABC'))
