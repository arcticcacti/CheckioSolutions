# "Feed Pigeons" downloaded: Sun Jul 31 18:33:25 2016
def checkio(foods):
    birds = 0
    minute = 0
    while foods > 0:
        foods -= birds
        minute += 1
        for i in range(minute):
            if foods > 0:
                birds += 1
                foods -= 1
    return birds
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
