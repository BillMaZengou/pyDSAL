"""
For an ordered list, Binary Search can be used
"""

def binarySearchNaive(a_list, item):
    first = 0
    last = len(a_list)
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

def binarySearchIteration(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binarySearchIteration(a_list[:midpoint], item)
            else:
                return binarySearchIteration(a_list[midpoint+1:], item)
