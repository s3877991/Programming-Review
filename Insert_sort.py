def insert_correctly(sorted_list, element):
    """
    insert element into sorted_list at a correct index
    and return the new list
    examples:
    insert_correctly([1, 3, 6], 5) # => [1, 3, 5, 6]
    insert_correctly([1, 3, 6], 0) # => [0, 1, 3, 6]
    insert_correctly([1, 3, 6], 8) # => [1, 3, 6, 8]
    """
    idx = 0
    while idx < len(sorted_list) and sorted_list[idx] < element:
        idx += 1
    if idx < len(sorted_list):
        sorted_list[idx:idx] = [element]
    else:
        sorted_list.append(element)
    return sorted_list

print(insert_correctly([1, 3, 6], 5))  # => [1, 3, 5, 6]
print(insert_correctly([1, 3, 6], 0))  # => [0, 1, 3, 6]
print(insert_correctly([1, 3, 6], 8))  # => [1, 3, 6, 8]

def insertion_sort(numbers):
    """
    sort numbers list and return sorted version
    """
    for idx in range(1, len(numbers)):
        new = insert_correctly(numbers[:idx], numbers[idx])
        numbers[:idx+1] = new
    return numbers

print(insertion_sort([7, 3, 1, 6, 5])) # => [1, 3, 5, 6, 7]

