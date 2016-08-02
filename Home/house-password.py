# "House password" downloaded: Sun Jul 31 18:31:52 2016
def checkio(data):

    if len(data) < 10:
        return False
    
    hasDigit = False;
    hasLower = False;
    hasUpper = False;
    
    for elem in data:
        if str.isdigit(elem):
            hasDigit = True
        elif str.islower(elem):
            hasLower = True
        elif str.isupper(elem):
            hasUpper = True
        
    return True if (hasDigit and hasLower and hasUpper) else False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"

