""" To check if all the elements in the list are same """
from typing import List, Any

def all_the_same(elements: List[Any]):
    return elements[1:] == elements[:-1]

if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    #"Asserts" for self-checking
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
