""" Return a list with  non unique elements only """
def nonUniqueElements(data: str) -> list :
    return [i for i in data if data.count(i)>1]

if __name__ == "__main__":
    assert isinstance(nonUniqueElements([1]), list), "The result must be a list"
    assert nonUniqueElements([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert nonUniqueElements([1, 2, 3, 4, 5]) == [], "2nd example"
    assert nonUniqueElements([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert nonUniqueElements([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"