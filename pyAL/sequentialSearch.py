def sequentialSearch(a_list, item):
    """
    Sequential Search for an unordered list
    """
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1

    return found

def orderedSequentialSearch(a_list, item):
    """
    Sequential Search for an ordered list
    """
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos += 1
    return found
