def find_min(l: list,i: int) -> int:
    """ Given list 'l' and index 'i', return the smallest element from position 'i' to the end of the list 'l'.

    :param l: list
    :param i: int
    :return: int
    """
    smallest_index = i
    #  Iterate through elements in position 'i' to the end of the list and record and compare the smallest element
    for j in range(i + 1, len(l)):

        if l[j] <l[smallest_index]:
            smallest_index = j

    return smallest_index


def selection_sort(l: list) -> None:
    """ Given list 'l', sort the list via. the selection sort method.

    :param l: list
    :return: None
    """
    #  Iterate through 'l' from the last to the first element and switch the correct and incorrect elements.

    for i in range(len(l) - 1):
        #  Find the smallest element from the remaining unsorted list.
        smallest_index = find_min(l, i)
        l[smallest_index], l[i] = l[i], l[smallest_index]

x = [1,2,4,2,3,1,5,6,1,3]
selection_sort(x)
print(x)