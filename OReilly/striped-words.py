# "Striped Words" downloaded: Sun Jul 31 18:45:06 2016
VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    # convert punctuation to whitespace and then pull out the 'words'
    text = "".join(map(lambda x: x if x.isalnum() else " ", text))
    # uppercase everything and ignore single-character words
    words = [w.upper() for w in text.split() if len(w) > 1]
    
    found = 0
    for word in words:
        # find out if the first char is a consonant
        expectCons = word[0] in CONSONANTS
        valid = True
        # for each letter, check if it's a consonant and whether one is expected
        for i in word:
            if expectCons == (i in CONSONANTS):
                # flip expectation after every valid char
                expectCons = not expectCons
            else:
                # word isn't alternately striped
                valid = False
                break
        found += valid
            
    return found

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"

