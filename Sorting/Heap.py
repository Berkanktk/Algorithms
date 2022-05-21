import heapq

A = [2, 1, 5, 4, 8, 6, 7, 9, 3]
heapq.heapify(A)

print("Min Heap:", A)

def max_heapify(A,k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l] > A[k]:
        largest = l
    else:
        largest = k
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != k:
        A[k], A[largest] = A[largest], A[k]
        max_heapify(A, largest)

def left(k):
    return 2 * k + 1

def right(i):
    return 2 * i + 2

def build_max_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        max_heapify(A,k)

build_max_heap(A)

print("Max Heap:", A)
