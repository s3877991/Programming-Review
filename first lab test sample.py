# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020C
# Assignment: 2
# Author: Nguyen Quang Duy (s3877991)
# Created date: 07/01/2021
# Last modified date: 09/01/2021

# 1) IMPORT LIBRARY:
import turtle


# 2) DEFINE FUNCTIONS:
def options():
    """Options are always shown in menu"""
    print("***************************")
    print("1. Top 3 numbers")
    print("2. Draw polygons")
    print("3. Exit")


def find_top3(numbers):
    """Convert a number string to a number list , sort all elements and find 3 largest numbers from that list"""
    number_character_list = numbers.split()
    number_list = []
    sorted_number_list = []
    for string_element in number_character_list:
        number_element = int(string_element)
        number_list.append(number_element)
    while number_list:
        minimum = number_list[0]
        for element in number_list:
            if element < minimum:
                minimum = element
        sorted_number_list.append(minimum)
        number_list.remove(minimum)
    max_index = len(sorted_number_list)
    top_3_list = sorted_number_list[max_index - 3: max_index + 1]
    return top_3_list


def draw_polygons(turtle, side, color):
    """Draw polygons with turtle and color them with color"""
    turtle.fillcolor(color)
    turtle.begin_fill()
    for point in range(side + 1):
        turtle.forward(100)
        turtle.left(180 * 2 / side)
    turtle.end_fill()
    turtle.setheading(0)


def outcome():
    """If users choose any suitable options, there are outcomes depending on those options"""
    if n == '1':
        numbers = input('Enter a string with a list of numbers: ')
        print('3 largest numbers in this string are:', find_top3(numbers))
    elif n == '2':
        index = 0
        win = turtle.Screen()
        duy = turtle.Turtle()
        color = ['red', 'yellow', 'green', 'blue']
        duy.up()
        duy.goto(-400, 0)
        duy.down()
        for side in range(3, 11):
            draw_polygons(duy, side, color[index % 4])
        win.exitonclick()
    elif n == '3':
        print("Program exits. Have a nice day!")


# 3) MAIN PROGRAM:
options()
n = input("Please enter an option (1/2/3): ")
outcome()
# If users write an invalid option, the program will announce "INVALID OPTION" and show the menu with
# new offer "RE-ENTER an option". But if this situation continues, the program will do that again and again
# until users write a valid option
while n != '1' and n != '2' and n != '3':
    print("Invalid option")
    options()
    n = input("Please re-enter an option (1/2/3): ")
    outcome()
