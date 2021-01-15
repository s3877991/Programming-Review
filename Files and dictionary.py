# FILE AND DICTIONARY EXERCISE:
# Exercise 1: INVENTORY
def read_inventory(file_name):
    """
    return a dictionary
    {product_name1: quantity1, product_name2, quantity2, ...}
    """
    file = open(file_name, 'r')
    dict = {}
    for line in file:
        product_name = line.split()
        quantity = product_name[0]
        value = ' '.join(product_name[1:])
        dict[quantity] = value
    file.close()
    return dict


def display_inventory(products):
    """
    products is a dictionary object
    {product_name1: quantity1, produc_tname2, quantity2, ...}
    """
    pass


my_products = read_inventory('D:\\RMIT 2020\\All Github Repositories\\Programming-Review\\inventory.txt')
print(my_products)
