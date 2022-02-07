# Algorithms
## Contents
### Sorting
* Bubble sort
* Insertion sort
* Merge sort
* Selection sort
### Searching
* Binary search
* Linear search
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
