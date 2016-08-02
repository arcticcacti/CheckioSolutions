# "Brackets" downloaded: Sun Jul 31 18:30:01 2016
from collections import deque
def checkio(expression):
    CLOSING_BRACKETS = {
        '}': '{',
        ')': '(',
        ']': '['}
    OPENING_BRACKETS = ('(', '{', '[')
    
    stack = deque()
    for char in expression:
        if char in OPENING_BRACKETS:
            stack.append(char)
        elif char in CLOSING_BRACKETS:
            if len(stack) and stack[-1] == CLOSING_BRACKETS[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"

