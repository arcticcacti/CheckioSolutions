# "Pawn Brotherhood" downloaded: Sun Jul 31 18:33:03 2016
def safe_pawns(pawns):
    
    def shift(char, amount):
        return chr(ord(char)+amount)
    
    safe = 0
    for col, row in [[pos[0], pos[1]] for pos in pawns]:
        # create a set of the two (hypothetical!) squares which defend this pawn
        heroes = set("".join([shift(col, i), shift(row, -1)]) for i in [1, -1])
        # check they're not both unoccupied
        safe += not heroes.isdisjoint(pawns)
            
    return safe

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

