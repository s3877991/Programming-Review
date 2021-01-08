# Ex 1
def index_maximum(numbers):
    """
    return the index of the maximum value in numbers
    """
    idx = 0
    for i in range(1, len(numbers)):
        if numbers[idx] < numbers[i]:
            idx = i
    return idx


print(index_maximum([1, 2, 3]))  # => [2]
print(index_maximum([1, 4, 2]))  # => [1]
print(index_maximum([1, 9, 6]))  # => [1]
