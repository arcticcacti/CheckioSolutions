# "Moore Neighbourhood" downloaded: Sun Jul 31 18:32:04 2016
def count_neighbours(grid, row, col):
    
    # get the max allowed row and column positions
    maxRow = len(grid) - 1
    maxCol = len(grid[0]) - 1
    
    # calculate the bounded extremes of the area to check
    top    = row-1 if row > 0      else row
    bottom = row+1 if row < maxRow else row
    left   = col-1 if col > 0      else col
    right  = col+1 if col < maxCol else col
    
    neighbours = 0
    # for each column, check each row (but ignore the middle starting square)
    for x in range(left, right+1):
        for y in range(top, bottom+1):
            if not (x == col and y == row) and grid[y][x] == 1:
                neighbours += 1
    
    return neighbours


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
