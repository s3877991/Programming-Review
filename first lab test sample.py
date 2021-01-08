# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020C
# Assignment: 2
# Author: Nguyen Quang Duy (s3877991)
# Created date: 07/01/2021
# Last modified date: 08/01/2021

# 1) IMPORT LIBRARY:
import turtle

# 2) DECLARE VARIABLES:
index = 0  # Initial index in a list


# 3) DEFINE FUNCTIONS:
def options():
    """Options are always shown in menu"""
    print("***************************")
    print("1. Top 3 numbers")
    print("2. Draw polygons")
    print("3. Exit")


def draw_polygons(turtle, side, color):
    """Draw polygons with turtle and color them with color"""
    turtle.fillcolor(color)
    for point in range(side + 1):
        turtle.begin_fill()
        turtle.forward(100)
        turtle.left(180 * 2 / side)
        turtle.end_fill()
    turtle.setheading(0)


def outcome():
    """If users choose any suitable options, there are outcomes depending on those options"""
    if n == '1':
        print('please wait')
    elif n == '2':
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


# 4) MAIN PROGRAM:
options()
n = input("Please enter an option (1/2/3): ")
outcome()
# If users write an invalid option, the program will announce "INVALID OPTION" and show the menu with
# new offer "RE-ENTER an option". But if this situation continues, the program will do that again and again
# until users write a valid option
while n != '1' and n != '2' and n != '3':
    options()
    print("Invalid option")
    n = input("Please re-enter an option (1/2/3): ")
    outcome()
