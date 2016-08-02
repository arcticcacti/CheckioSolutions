# "Xs and Os Referee" downloaded: Sun Jul 31 18:32:39 2016
def checkio(game_result):
    
    winner = "D"
    
    def checkThree(coords):
        line = [game_result[row][col] for row, col in coords]
        mark = line[0]
        if line.count(mark) == 3:
            return mark
        else:
            return ""
        
    # generate horizontal/vertical lines to check
    lines = []
    for pos in range(3):
        lines.append([(row,pos) for row in range(3)])
        lines.append([(pos,col) for col in range(3)])
        
    # generate diagonals
    lines.append([(coord, coord) for coord in range(3)])
    lines.append([(coord, 2-coord) for coord in range(3)])
    
    # check em
    for line in lines:
        result = checkThree(line)
        if result in ["X", "O"]:
            return result
        
    return "D"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
