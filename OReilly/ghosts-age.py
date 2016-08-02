# "Ghosts age" downloaded: Sun Jul 31 18:45:16 2016
def checkio(opacity):
    fibs = (1, 1)
    def isFib(age, fibs):
        if age == 0:
            return True
        while age > fibs[1]:
            fibs = (fibs[1], fibs[0]+fibs[1])
        return age == fibs[1]

    ageOpacity = 10000
    for age in range(5000):
        ageOpacity += (1 * (not isFib(age, fibs))) - (age * isFib(age, fibs))
        if ageOpacity == opacity:
            return age
        
    return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
