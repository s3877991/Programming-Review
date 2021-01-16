# FILE AND DICTIONARY EXERCISE:
# Exercise 1: INVENTORY
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
