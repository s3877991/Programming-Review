# import turtle


# def draw_polygons(turtle, side, color):
#    """Draw polygons with turtle and color them with color"""
#    turtle.fillcolor(color)
#    turtle.begin_fill()
#    for point in range(side + 1):
#        turtle.forward(100)
#        turtle.left(180 * 2 / side)
#    turtle.end_fill()
#    turtle.setheading(0)


# win = turtle.Screen()
# duy = turtle.Turtle()
# color = ['red', 'yellow', 'green', 'blue']
# duy.up()
# duy.goto(-400, 0)
# duy.down()
# index = 0
# for side in range(3, 11):
#    double_color = color * side
#    draw_polygons(duy, side, double_color[index])
#    index += 1

# win.exitonclick()


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


def second_largest(numbers):
    """From a sorted list of numbers, find the second largest one"""
    idx = -1
    while numbers:
        if numbers[idx] == numbers[idx - 1]:
            idx += -1
        elif numbers[idx] > numbers[idx - 1]:
            return numbers[idx - 1]


print(second_largest([1, 2, 2, 3, 4, 4]))
print(second_largest([1, 2, 3, 4]))


def read_inventory(file_name):
    f = open(file_name, 'r')
    products = {}
    for line in f:
        words = line.split()
        product_name = words[0]
        quantity = int(words[1])
        if product_name in products:
            products[product_name] = products[product_name] + quantity
        else:
            products[product_name] = quantity
    f.close()
    return products


def display_inventory(products):
    for product_name, quantity in products.items():
        print(product_name, "has", quantity, "items")


my_products = read_inventory('inventory.txt')
display_inventory(my_products)


res = []
for number in range(1000, 3001):
    string = str(number)
    if (int(string[0]) % 2 == 0) and (int(string[1]) % 2 == 0) and (int(string[2]) % 2 == 0) and (int(string[3]) % 2 == 0):
        res.append(string)
print(','.join(res))
