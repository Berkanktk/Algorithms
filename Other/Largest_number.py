def largest_num(array):
    temp = 0
    for n in array:
        if temp < n:
            temp = n
    return temp
