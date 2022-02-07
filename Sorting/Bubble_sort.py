def bubble_sort(array):
    swapped = True  # Set flag to run the while loop until the list is sorted

    while swapped:
        swapped = False  # Sets the flag to false and stops the algorithm if the if-statement doesn't run
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True  # If the if statement runs, a swap will be made and the algorithm will run again
