# Algorithms
## Contents
### Sorting
* Bubble sort
  * Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
* Insertion sort
  * Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands.
* Merge sort
  * Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.
* Selection sort
  * The selection sort algorithm sorts an array by repeatedly finding the minimum element from unsorted part and putting it at the beginning.
### Searching
* Binary search
  * Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one. 
* Linear search
  * A linear search is the simplest method of searching a data set. Starting at the beginning of the data set, each item of data is examined until a match is made
### Other
* Largest number (Finds the largest number inside an array)
```python
def largest_num(array):
    temp = 0
    for n in array:
        if temp < n:
            temp = n
    return temp
```
* Random list (Generates a random list with a user selected length between 0-100)
```python
import random


def random_list(length):
    gen_list = []
    for i in range(0, length):
        gen_list.append(random.randint(0, 100))

    return gen_list
```
* Stalin sort (A sorting algorithm that simply remove the integer from the array if its lower than the previous int)
```python
from Other.Random_list import random_list


def stalin_sort(array):
    temp = array[0]
    sortedList = []
    for n in array:
        if temp <= n:
            sortedList.append(n)
            temp = n
    return sortedList
```
### main.py
* Different pre-made test functions to test the different algorithms.
