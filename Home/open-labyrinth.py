# "Open Labyrinth" downloaded: Sun Jul 31 18:34:09 2016
#Your code here
#You can import some modules or create additional functions


def checkio(newmap):
    start = (1, 1)
    goal  = (10,10)
    
    neighbourinos = {"W": (0,-1),
                     "E": (0, 1),
                     "N": (-1,0),
                     "S": (1, 0)}
    
    queue=[start]
    while queue:
        (row, col) = queue.pop(0)
        for dir, (y, x) in neighbourinos.items():
            if newmap[row+y][col+x] == 0:
                newmap[row+y][col+x] = dir
                if (row+y, col+x) == goal:
                    break
                else:
                    queue.append((row+y, col+x))

    y, x = goal
    path = []
    while (y, x) != start:
        dir = newmap[y][x]
        path.append(dir)
        y -= neighbourinos[dir][0]
        x -= neighbourinos[dir][1]
    
    path.reverse()
    result = "".join(path)
