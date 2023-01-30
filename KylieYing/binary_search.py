def binary_search_MP(l, target):
    # the search works OK, but the retrieval of the correct index does not
    if len(l) == 0:
        index = -1
    elif len(l) == 1:
        if l[0] == target:
            index = 0
        else:
            index = -1
    else:
        middle = len(l) // 2
        if l[middle] == target:
            index = middle
        elif l[middle] > target:
            index = binary_search(l[:middle], target)
            if index >= 0:
                index = len(l) - (index + middle) # wrong
        else:
            index = binary_search(l[middle + 1:], target)
            if index >= 0:
                index = len(l) + (index - middle) # wrong
    return index


def binary_search(l, target, low=None, high=None):
    if low == None:
        low = 0
    if high == None:
        high = len(l) - 1

    if high < low:
        return -1

    middle = (low + high) // 2

    if l[middle] == target:
        return middle
    elif l[middle] > target:
        return binary_search(l, target, low, middle - 1)
    else:
        return binary_search(l, target, middle + 1, high)



my_list = [1, 20, 40, 50, 60, 105]
print(binary_search(my_list, 40))