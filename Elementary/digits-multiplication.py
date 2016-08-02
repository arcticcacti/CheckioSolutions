# "Digits Multiplication" downloaded: Sun Jul 31 18:37:26 2016
def checkio(number):
    number = str(number)
    total = 1
    for i in range(len(number)):
        if (number[i] != "0"):
            total *= int(number[i])
        
    return total

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1

