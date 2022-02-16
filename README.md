# Algorithms
## Speeds
Problem size: 50

Winner = Shortest sorting time  
Fast = Sorting speed is almost the same as the winner  
Slowest = Longest sorting time

|  | Insertion | Selection | Bubble | Shell | Merge | Heap | Quick | Quick3 |
|---|---|---|---|---|---|---|---|---|
| Random |  | Slowest |  | Fast | Fast | Winner |  |  |
| Nearly sorted | Winner | Slowest |  |  |  |  |  |  |
| Reversed |  | Slowest |  | Winner |  |  |  |  |
| Few Unique |  | Slowest |  |  |  |  |  | Winner |

Explanations:
### Random
A random initial order is often used to evaluate sorting algorithms in order to elucidate the “typical” case and to facilitate mathematical analysis. For some applications, however, this does not represent the typical case, so conclusions drawn here do not generalize.

Here we see the vast difference in speed between the O(n2) elementary sorting algorithms (insert, selection, bubble) and the more advanced algorithms.

Source: [Link](https://www.toptal.com/developers/sorting-algorithms)

### Nearly sorted
Sorting nearly sorted data is quite common in practice. Some observations:

* Insertion sort is the clear winner on this initial condition.
* Bubble sort is fast, but insertion sort has lower overhead.
* Shell sort is fast because it is based on insertion sort.
* Merge sort, heap sort, and quick sort do not adapt to nearly sorted data.

Insertion sort provides a O(n2) worst case algorithm that adapts to O(n) time when the data is nearly sorted. One would like an O(n·lg(n)) algorithm that adapts to this situation; smoothsort is such an algorithm, but is complex. Shell sort is the only sub-quadratic algorithm shown here that is also adaptive in this case.

### Reversed
Sorting an array that is initially in reverse sorted order is an interesting case because it is common in practice and it brings out worse-case behavior for insertion sort, bubble sort, and shell sort.

### Few Unique
Sorting an array that consists of a small number of unique keys is common in practice. One would like an algorithm that adapts to O(n) time when the number of unique keys is O(1). In this example, there are 4 unique keys.

The traditional 2-way partitioning quicksort exhibits its worse-case O(n2) behavior here. For this reason, any quicksort implementation should use 3-way partitioning, where the array is partitioned into values less than, equal, and greater than the pivot. Because the pivot values need not be sorted recursively, 3-way quick sort adapts to O(n) time in this case.  

Shell sort also adapts to few unique keys, though I do not know its time complexity in this case.

## Contains
### Sorting
**Bubble sort**  
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

**Insertion sort**  
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands.

**Merge sort**  
Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.

**Selection sort**  
The selection sort algorithm sorts an array by repeatedly finding the minimum element from unsorted part and putting it at the beginning.

### Searching
**Binary search**  
Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one. 

**Linear search**  
A linear search is the simplest method of searching a data set. Starting at the beginning of the data set, each item of data is examined until a match is made

### Other
**Largest number** (Finds the largest number inside an array)
```python
def largest_num(array):
    temp = 0
    for n in array:
        if temp < n:
            temp = n
    return temp
```
**Random list** (Generates a random list with a user selected length between 0-100)
```python
import random


def random_list(length):
    gen_list = []
    for i in range(0, length):
        gen_list.append(random.randint(0, 100))

    return gen_list
```
**Stalin sort** (A sorting algorithm that simply remove the integer from the array if its lower than the previous int)
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
