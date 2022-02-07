# My version of stalin sort
from Other.Random_list import random_list


def stalin_sort(array):
    temp = array[0]
    sortedList = []
    for n in array:
        if temp <= n:
            sortedList.append(n)
            temp = n
    return sortedList


if __name__ == '__main__':
    ordered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sorted_list = stalin_sort(ordered_list)
    print("Original:", ordered_list, "\nSorted:", sorted_list, "\n")

    reversed_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    sorted_list = stalin_sort(reversed_list)
    print("Original:", reversed_list, "\nSorted:", sorted_list, "\n")

    mixed_list = [1, 3, 2, 5, 4, 7, 6, 9, 8]
    sorted_list = stalin_sort(mixed_list)
    print("Original:", mixed_list, "\nSorted:", sorted_list, "\n")

    test_list = [1, 5, 2, 4]
    sorted_list = stalin_sort(test_list)
    print("Original:", test_list, "\nSorted:", sorted_list, "\n")

    random = random_list(10)
    sortedRandomList = stalin_sort(random)
    print("Original:", random, "\nSorted:", sortedRandomList, "\n")
