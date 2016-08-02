# "The Most Wanted Letter" downloaded: Sun Jul 31 18:32:22 2016
def checkio(text):

    lowered = str.lower(text)
    highest = 0
    highestChar = ""
    
    for i in range(len(lowered)):
        char = lowered[i]
        if str.isalpha(char):
            num = lowered.count(lowered[i])
            if num > highest or (num == highest and lowered[i] < highestChar):
                highest = num
                highestChar = lowered[i]
            
    return highestChar

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

