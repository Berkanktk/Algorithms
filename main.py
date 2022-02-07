from Other.Largest_number import largest_num
from Other.Random_list import random_list
from Other.Stalin_sort import stalin_sort
from Sorting.Bubble_sort import bubble_sort
from Sorting.Insertion_sort import insertion_sort
from Sorting.Merge_sort import merge_sort
from Sorting.Selection_sort import selection_sort
from Search.Binary_search import binary_search_recursive
from Search.Binary_search import binary_search_iterative
from Search.Linear_search import linear_search


def largest_num_test():
    a = random_list(8)
    print('Original list:', a)
    print('Largest number:', largest_num(a))


def bubble_sort_test():
    random = random_list(8)
    print('Original:', random)

    bubble_sort(random)

    sortedlist = []
    for n in random:
        sortedlist.append(n)

    print('Sorted:', sortedlist)


def insertion_sort_test():
    random = random_list(8)
    print('Original:', random)

    insertion_sort(random)

    sortedlist = []
    for n in random:
        sortedlist.append(n)

    print('Sorted:', sortedlist)


def stalin_sort_test():
    random = random_list(8)
    print('Original:', random)

    print('Sorted:', stalin_sort(random))


def merge_sort_test():
    random = random_list(8)
    print('Original:', random)

    merge_sort(random)

    sortedlist = []
    for n in random:
        sortedlist.append(n)

    print('Sorted:', sortedlist)


def selection_sort_test():
    random = random_list(8)
    print('Original:', random)

    selection_sort(random)

    sortedlist = []
    for n in random:
        sortedlist.append(n)

    print('Sorted:', sortedlist)


def binary_search_recursive_test():
    a = random_list(80)
    print(a)

    print(binary_search_recursive(a, 0, len(a)-1, 5))


def binary_search_iterative_test():
    a = random_list(80)
    print(a)

    print(binary_search_iterative(a, 5))


def linear_search_test():
    a = random_list(80)
    print(a)

    search = linear_search(a, 5)

    print(search)


if __name__ == '__main__':
    bubble_sort_test()