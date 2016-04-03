def merge(list1: list, list2: list) -> list:
    """Return sorted merged list of list 1 and list 2.

    :param list1:
    :param list2:
    :return: list

    """
    result = []
    i = 0
    j = 0
    #  Iterate through each element and append the smaller element of each list to the resulting list.
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    #  Append the remaining lists to the resulting list.
    result.extend(list1[i:])
    result.extend(list2[j:])
    return result


def merge_sort(l: list) -> list:
    """Return sorted list 'l' using the merge sort method.

    :param l: list
    :return: list
    """
    #  Trap for lists with one or fewer elements.
    if len(l) <= 1:
        return l[:]
    #  Divide the list into 2
    mid = len(l) // 2
    first = l[mid:]
    second = l[:mid]
    #  Recursively sort smaller lists and merge the two resulting lists.
    left = merge_sort(first)
    right = merge_sort(second)
    return merge(left, right)

x = [1,2,4,2,3,1,5,6,1,3]
l = merge_sort(x)
print(l)