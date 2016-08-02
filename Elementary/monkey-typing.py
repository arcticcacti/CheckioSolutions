# "Monkey Typing" downloaded: Sun Jul 31 18:36:06 2016
def count_words(text, words):
 #   total = 0
 #   for word in words:
 #       if str.lower(text).find(word) != -1:
 #          total += 1
 #   return total
    return len([1 for word in words if str.lower(text).find(word) != -1])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"

