# "Index Power" downloaded: Sun Jul 31 18:34:40 2016
def index_power(array, n):
    if len(array) < n+1:
        return -1
    result = 1
    for i in range(n):
        result *= array[n]
    
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"

