#sum even index numbers in list and add the final element in list
from itertools import islice
def checkio(array: list) -> int:
    """
        sums even-indexes elements and multiply at the last
    """
    return sum([i for i in islice(array, None, None, 2)]) * array[-1] if array else 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    #array = [0, 1, 2, 3, 4, 5]
    #print(sum([ array[i] for i in range(0,len(array), 2)]) * array[-1]) 
    print(checkio([0, 1, 2, 3, 4, 5]))
    
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"