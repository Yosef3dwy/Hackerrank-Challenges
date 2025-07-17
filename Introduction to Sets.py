def average(array):
    # your code goes here
    array = set(array)
    Av = 0
    size = 0
    for x in array:
        Av += x
        size += 1
        
    return Av / size