# "Number Base" downloaded: Sun Jul 31 18:38:23 2016
def checkio(str_number, radix):
    # create a value lookup sequence, truncated to the max value per the radix
    lookup = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:radix]
    
    # iterate over every place in the number
    total = 0
    for i in range(len(str_number)):
        # walk right to left through the number - end if a digit is not found
        value = lookup.find(str_number[-1 -i])
        if value == -1:
            return -1
        # each place represents the radix raised to a power, and the digit
        # is a multiple of that (e.g. in base-10, 303 is 3*(10^2) + 3*(10^0)
        total += (radix**i) * value
        
    return total

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"

