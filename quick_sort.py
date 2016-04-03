def partition(l: list) -> int:
    """  Partition list 'l' using the right-most element as the pivot.

    :param l: list
    :return:
    """
    if len(l) <= 1:
        return 1
    pivot = l[len(l) - 1]
    pivot_index = len(l) - 1
    i = len(l) - 1
    while i >= 0:
        if l[i] > pivot:
            l.append(l[i])
            del l[i]
            pivot_index -= 1
        i -= 1
    return pivot_index


def quick_sort(l: list) -> list:
    result = []
    if len(l) <= 1:
        return l[:]
    pivot = partition(l)
    left = l[:pivot]
    right = l[pivot:]
    result.extend(quick_sort(left))
    result.extend(quick_sort(right))
    return result

x = [1,2,4,2,3,1,5,6,1,3]
l = quick_sort(x)
print(l)