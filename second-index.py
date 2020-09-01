def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    out = None
    first = text.find(symbol)
    second = text[first+1:].find(symbol)
    if (first >=0) and (second >=0):
        out = second + first + 1
    return out


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))
    

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"