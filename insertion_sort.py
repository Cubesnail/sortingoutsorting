def insert(l: list, i: int) -> None:
    ''' Given index 'i' in list 'l' take an element and insert it into the correct location
    :param l: list
    :param i: index
    :return: None
    '''
    v = l[i]
    #  Record element into variable 'v'
    while i > 0 and l[i - 1] > v:
        #  Find the insertion point going from greatest to smallest from right to left in 'l'
        l[i] = l[i -1]
        #  Move each element one position right
        i -= 1

    l[i] = v
    #  Insert the recorded element into the correct position


def insertion_sort(l: list) -> None:
    """ Given list 'l', sort it via. the insertion sort method.
    :param l: list
    :return: None
    """
    #  Iterate through each element in the list and insert it into the correct position.
    for i in range(1,len(l)):
        insert(l,i)

x = [1,2,4,2,3,1,5,6,1,3]
insertion_sort(x)
print(x)