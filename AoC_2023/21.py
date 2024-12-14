
import numpy as np

def read_input():
    file = open("21.txt", "r")
    lines = []
    while True:
        line = file.readline()[:-1]
        if not line:
            break
        lines.append(list(line))
    return lines

def part1():
    grid = read_input()

    # Find the starting point
    x, y = 0, 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                x, y = i, j
                break

    grid = [list(row) for row in grid]

    queue = [(x, y)]
    for i in range(65):
        new_queue = []
        while True:
            if not queue:
                break
            x, y = queue.pop()
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                continue
            if type(grid[x][y]) == int or grid[x][y] == "#":
                continue
            if grid[x][y] == "." or grid[x][y] == "S":
                grid[x][y] = i
                new_queue.append((x-1, y))
                new_queue.append((x+1, y))
                new_queue.append((x, y-1))
                new_queue.append((x, y+1))
        queue = new_queue

    print(i)
    for row in grid:
        print(''.join(["{:3s}".format(str(cell)) for cell in row]))

    counter = 0
    for row in grid:
        for cell in row:
            if type(cell) == int and cell % 2 == 0:
                counter += 1
    print(counter)

def steps_to_reach_all_positions(grid, start_x, start_y):
    ways = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = [(start_x, start_y)]
    tmp_grid = [list(row) for row in grid]
    i = 0
    while True:
        new_queue = []
        while True:
            if not queue:
                break
            x, y = queue.pop()
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                continue
            if type(grid[x][y]) == int or grid[x][y] == "#":
                continue
            if grid[x][y] == "." or grid[x][y] == "S":
                grid[x][y] = i
                new_queue.append((x-1, y))
                new_queue.append((x+1, y))
                new_queue.append((x, y-1))
                new_queue.append((x, y+1))
        queue = new_queue
        i += 1
        if tmp_grid == grid:
            print(i)
            break
        tmp_grid = [list(row) for row in grid]
    return grid


def part2():
    grid = read_input()
    x = steps_to_reach_all_positions(grid, len(grid)//2, len(grid[0])-1)
    sum = 0
    for row in x:
        for cell in row:
            if type(cell) == int and cell % 2 == 0:
                sum += 1

    odd = sum

    sum = 0
    for row in x:
        for cell in row:
            if type(cell) == int and cell % 2 == 1:
                sum += 1

    even = sum

    even_half_grid_sum = 0 
    for row in x:
        for cell in row:
            if type(cell) == int and cell % 2 == 0 and cell > len(grid) // 2:
                even_half_grid_sum += 1

    odd_half_grid_sum = 0
    for row in x:
        for cell in row:
            if type(cell) == int and cell % 2 == 1 and cell > len(grid [0]) // 2:
                odd_half_grid_sum += 1

    print(odd, even, odd_half_grid_sum, even_half_grid_sum)
    x = 26501365 // len(grid)
    sum = odd * x**2 + even * (x+1)**2 - (x + 1) * odd_half_grid_sum + x * even_half_grid_sum 

    print(sum)

part2()