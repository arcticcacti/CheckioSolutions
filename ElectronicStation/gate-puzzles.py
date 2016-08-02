# "Moria doors" downloaded: Sun Jul 31 18:30:58 2016
import string, itertools
from collections import defaultdict


def get_words(message):
    clean = message.lower()
    for c in string.punctuation:
        clean = clean.replace(c, ' ')
    return clean.split()
    
    
def score_likeness(word1, word2):
    score = 10 * (word1[0] == word2[0]) + 10*(word1[-1] == word2[-1])
    score += 30 * min(len(word1), len(word2)) / max(len(word1), len(word2))
    score += 50 * len(set(word1).intersection(word2)) / len(set(word1).union(word2))
    return score


def find_word(message):
    words = get_words(message)
    scores = [[] for _ in words]
    for i, j in itertools.permutations(range(len(words)), 2):
        scores[i].append(score_likeness(words[i], words[j]))
    # walk backwards through the list of scores, averaging each group, and get the first instance of the max
    best_index = max(range(len(scores)-1, -1, -1), key=lambda x: sum(scores[x])/len(scores[x]))
    return words[best_index]
        
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word("Friend Fred and friend Ted.") == "friend", "FRIENDS"
    assert find_word("Speak friend and enter.") == "friend", "Friend"
    assert find_word("Beard and Bread") == "bread", "Bread is Beard"
    assert find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
