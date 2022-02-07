def selection_sort(array):
    for i in range(len(array)):
        minimum = i
        for j in range(i + 1, len(array)):
            if array[minimum] > array[j]:
                minimum = j

        array[i], array[minimum] = array[minimum], array[i]
