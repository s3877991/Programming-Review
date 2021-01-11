# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020C
# Assignment: 2
# Author: Nguyen Quang Duy (s3877991)
# Created date: 09/01/2021
# Last modified date: 09/01/2021


# Menu function:
def menu():
    print('============')
    print('1. Spell checker')
    print('2. Second largest')
    print('3. RMIT Cipher')
    print('4. Exit')


# Problem 1: Check spelling.
def spell_check(words, dict):
    pass


# Problem 2: Second largest.
def second_largest(numbers):
    """From a sorted list of numbers, find the second largest one"""
    idx = -1                                      # initial index
    while numbers:
        if numbers[idx] == numbers[idx - 1]:      # if the last element is equal to previous element in a sorted number
            idx += -1                             # list, move to that previous element to continue the process
        elif numbers[idx] > numbers[idx - 1]:     # otherwise, that previous element is the second largest number in
            return numbers[idx - 1]               # that list


# Problem 3: RMIT Cipher.
def rmit_encrypt(plain_text, key):
    """From a string of plain text, encrypt them by adding or subtracting its alphabet ordinal numbers with key"""
    character_string = ""
    encrypted_text = ""
    for index in range(26):                       # create a character string by double a string with alphabet
        character_string = character_string + chr(ord('A') + index)
    character_string = character_string * 2
    for character in plain_text:                  # based on character string and key, encrypt the characters in plain
        index = character_string.find(character)  # text and record new encrypt string
        encrypted_text = encrypted_text + character_string[index + key]
    print('The encrypted text is: ', encrypted_text)


# MAIN PROGRAM:
menu()
n = input('Your choice: ')
while n == '1' or n == '2' or n == '3':         # When users choose option 1, 2 or 3, the program call the functions
    if n == '1':                                # and display the returned value, and the show the menu again.
        name = ["Nguyen", "Quang", "Duy"]
        dict = ["nguyen", "quang", "duy"]
        spell_check(name, dict)
        menu()
        n = input('Your choice: ')
    elif n == '2':
        number = [1, 3, 7, 7, 8, 9, 9]
        x = second_largest(number)
        print('The second largest number is:', x)
        menu()
        n = input('Your choice: ')
    elif n == '3':
        plain_text = "NGUYENQUANGDUY"
        key = -5
        rmit_encrypt(plain_text, key)
        menu()
        n = input('Your choice: ')
    else:                                       # When users selects any values other than 1, 2, 3, the program exits
        pass
