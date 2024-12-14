
import numpy as np

def read_input():
    file = open("6.txt", "r")
    grid = []
    while True:
        line = file.readline()[:-1]
        if not line:
            break
        grid.append(line)

    return grid

def part1():
    grid = read_input()
    x, y = 0, 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                x, y = i, j
                break
        
        if x != 0 and y != 0:
            break

    mask = np.zeros((len(grid), len(grid[0])), dtype=bool)
    ways = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    way_index = 0
    while True:
        mask[x][y] = True
        if x + ways[way_index][0] < 0 or y + ways[way_index][1] < 0 or x + ways[way_index][0] >= len(grid) or y + ways[way_index][1] >= len(grid[0]):
            print(x, y)
            break
        if grid[x][y] == "#":
            raise Exception("In wall")
        
        if grid[x + ways[way_index][0]][y + ways[way_index][1]] == "#":
            way_index = (way_index + 1) % 4

        x, y = x + ways[way_index][0], y + ways[way_index][1]

    print(np.sum(mask))
    return mask
        

def part2(mask):
    grid = read_input()

    start_x, start_y = 0, 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                start_x, start_y = i, j
                break
        
        if start_x != 0 and start_x != 0:
            break

    ways = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != ".":
                continue
            if not mask[i][j]:
                continue
            print("Extra wall:", i, j)
            grid[i] = grid[i][:j] + "#" + grid[i][j+1:]

            way_index = 0
            x, y = start_x, start_y

            states = []

            while True:

                if x + ways[way_index][0] < 0 or y + ways[way_index][1] < 0 or x + ways[way_index][0] >= len(grid) or y + ways[way_index][1] >= len(grid[0]):
                    break
                if grid[x][y] == "#":
                    print(x, y)
                    print(grid) 
                    raise Exception("In wall")
                
                if (x, y, way_index) in states:
                    print(x, y)
                    break
                #print("Position:", x, y)
                states.append((x, y, way_index))
                
                while grid[x + ways[way_index][0]][y + ways[way_index][1]] == "#":
                    way_index = (way_index + 1) % 4
                
                x, y = x + ways[way_index][0], y + ways[way_index][1]


            grid[i] = grid[i][:j] + "." + grid[i][j+1:]
            if (x, y, way_index) in states:
                res += 1
    
    print(res)

mask = part1()
part2(mask)
