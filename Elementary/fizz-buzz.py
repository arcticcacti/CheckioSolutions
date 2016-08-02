# "Fizz Buzz" downloaded: Sun Jul 31 18:34:24 2016
def checkio(number):
    # the (factor, text) list could be pulled out and defined here
    # if you wanted to add some extra Fuzzing and Bazzing
    
    # collect all the fizzing and buzzing in a list
    output = []
    for factor, text in [(3, "Fizz"), (5, "Buzz")]:
        if number % factor == 0:
            output.append(text)
    
    # if there's any output string it together, otherwise return the number
    return " ".join(output) or str(number)

#Some hints:
#Convert a number in the string with str(n)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"

