# "Binary count" downloaded: Sun Jul 31 18:38:09 2016
def checkio(number):
    return bin(number).count("1")

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9

