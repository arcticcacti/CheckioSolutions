# "Three words" downloaded: Sun Jul 31 18:36:29 2016
def checkio(words):
    run = 0
    for word in words.split():
        run = run+1 if word.isalpha() else 0
        if run == 3:
                return True    
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"

