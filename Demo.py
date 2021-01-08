import turtle


def draw_polygons(turtle, side, color):
    """Draw polygons with turtle and color them with color"""
    turtle.fillcolor(color)
    turtle.begin_fill()
    for point in range(side + 1):
        turtle.forward(100)
        turtle.left(180 * 2 / side)
    turtle.end_fill()
    turtle.setheading(0)


win = turtle.Screen()
duy = turtle.Turtle()
color = ['red', 'yellow', 'green', 'blue']
duy.up()
duy.goto(-400, 0)
duy.down()
for index in color:
    for side in range(3, 11):
        draw_polygons(duy, side, color[index % 4])
win.exitonclick()

# def find_top_3(numbers):
#    number_character_list = numbers.split()
#    list = []
#    sorted_list = []
#    for string_element in number_character_list:
#        number_element = int(string_element)
#        list.append(number_element)
#    while list:
#        min = list[0]
#        for phan_tu in list:
#            if phan_tu < min:
#                min = phan_tu
#        sorted_list.append(min)
#        list.remove(min)
#    max_index = len(sorted_list)
#    top_3_list = sorted_list[max_index - 3: max_index + 1]
#    return top_3_list


# numbers = '1 3 5 6 2 4 5 7'
# print(find_top_3(numbers)))
