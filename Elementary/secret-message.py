# "Secret Message" downloaded: Sun Jul 31 18:36:17 2016
def find_message(text):
    caps = ""
    for i in range(len(text)):
        if text[i].isupper():
            caps += text[i]
    return caps

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"

