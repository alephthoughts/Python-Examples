import string

def mostWantedLetter(text: str) -> str:
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)

if __name__ == '__main__':
    print("Example:")
    print(mostWantedLetter("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert mostWantedLetter("Hello World!") == "l", "Hello test"
    assert mostWantedLetter("How do you do?") == "o", "O is most wanted"
    assert mostWantedLetter("One") == "e", "All letter only once."
    assert mostWantedLetter("Oops!") == "o", "Don't forget about lower case."
    assert mostWantedLetter("AAaooo!!!!") == "a", "Only letters."
    assert mostWantedLetter("abe") == "a", "The First."
    print("Start the long test")
    assert mostWantedLetter("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")