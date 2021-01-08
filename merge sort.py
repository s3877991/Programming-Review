def merge(list1, list2):
    """
    takes 2 sorted lists and returns a new combined sorted list
    Examples:
    merge([1, 5, 9], [3, 7, 10]) # returns [1, 3, 5, 7, 9, 10]
    merge([1, 2, 3], [4, 5, 6]) # returns [1, 2, 3, 4, 5, 6]
    merge([], [4, 5, 6]) # returns [4, 5, 6]
    """
    tmp_list = []
    n1 = len(list1)
    n2 = len(list2)

    # Merge the list1 and list2 into tmp_list
    pointer1 = 0  # Initial index of first list
    pointer2 = 0  # Initial index of second list

    while pointer1 < n1 and pointer2 < n2:
        if list1[pointer1] <= list2[pointer2]:
            tmp_list.append(list1[pointer1])
            pointer1 += 1
        else:
            tmp_list.append(list2[pointer2])
            pointer2 += 1

    # Copy the remaining elements of first list, if there
    # are any
    while pointer1 < n1:
        tmp_list.append(list1[pointer1])
        pointer1 += 1

    # Copy the remaining elements of second list, if there
    # are any
    while pointer2 < n2:
        tmp_list.append(list2[pointer2])
        pointer2 += 1

    return tmp_list

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid_idx = len(my_list) // 2
    first = merge_sort(my_list[:mid_idx])
    second = merge_sort(my_list[mid_idx:])
    return merge(first, second)


print(merge_sort([1, 5, 9, 3, 7, 10]))