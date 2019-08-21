""" To check if password is of length 10, one digit, one upper case and one lower case letter."""

def checkPassword(data: str) -> bool:
    upper_fl = False
    lower_fl = False
    digit_fl = False

    if len(data) < 10:
        return False
    else:
        for c in data:
            if c.isupper():
                upper_fl = True
            if c.islower():
                lower_fl = True
            if c.isdigit():
                digit_fl = True
        return upper_fl and lower_fl and digit_fl

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkPassword('A1213pokl') == False, "1st example"
    assert checkPassword('bAse730onE4') == True, "2nd example"
    assert checkPassword('asasasasasasasaas') == False, "3rd example"
    assert checkPassword('QWERTYqwerty') == False, "4th example"
    assert checkPassword('123456123456') == False, "5th example"
    assert checkPassword('QwErTy911poqqqq') == True, "6th example"
