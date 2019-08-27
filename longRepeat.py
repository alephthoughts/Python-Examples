from itertools import groupby
def longRepeat(line):
    return max((sum(1 for _ in g) for k, g in groupby(line)), default=0)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert    longRepeat('sdsffffse') ==4, "First"
    assert longRepeat('ddvvrwwwrggg') == 3, "Second"#    assert long_repeat('abababaab') == 2, "Third"
    assert longRepeat('') == 0, "Empty"