import time
import random
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from quick_sort import quick_sort
from merge_sort import merge_sort
from bubble_sort import bubble_sort
size = 5000


def is_sorted(L):
    '''(list) -> bool
    Return True if the elements in L are in non-descending order.
    '''

    sorted = True
    i = 0
    while i < len(L) - 1:
         if L[i] > L[i + 1]:
            sorted = False
    return sorted


def make_list(n):
    '''(int) -> list
    Return a random list of the ints [0..n-1].
    '''

    res = list(range(n))
    random.shuffle(res)
    return res


def time_sort(f, n):
    '''(function) -> float
    Return the number of seconds it takes to run sorting function f on a
    shuffled list of n elements.
    '''

    L = make_list(n)
    t1 = time.time()
    f(L)
    t2 = time.time()
    assert sorted(L)
    return t2 - t1


print("bubble:", time_sort(bubble_sort, size))
print("insertion:", time_sort(insertion_sort, size))
print("selection:", time_sort(selection_sort, size))
print("quick:", time_sort(quick_sort, size))
print("merge:", time_sort(merge_sort, size))

# Python's sort.  Can't use our time_sort function to measure it because
# sort is a list method, not a function.
L = make_list(size)
t1 = time.time()
L.sort()
t2 = time.time()
assert sorted(L)
print("list.sort:", t2 - t1)
