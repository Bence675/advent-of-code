
from base import *
from collections import deque
import numpy as np

def part1():
    data = readers.read_input("12.txt")

    visited = set()
    sum = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (i, j) in visited:
                continue
            stack = [(i, j)]
            area = 0
            perimeter = 0
            while stack:
                x, y = stack.pop()
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                
                area += 1
                perimeter += 4
                for x_, y_ in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if utils.is_index_in_matrix((x_, y_), data, debug=True):

                        if data[x_][y_] == data[x][y]:
                            stack.append((x_, y_))
                            perimeter -= 1
            sum += area * perimeter

    print(sum)

part1()

def walls(cells, data):
    corners = 0
    for i in range(len(data)+1):
        for j in range(len(data[0])+1):
            color_count = 0
            for x, y in [(i, j), (i-1, j), (i, j-1), (i-1, j-1)]:
                if utils.is_index_in_matrix((x, y), data):
                    if (x, y) in cells:
                        color_count += 1
            if color_count == 0:
                pass
            elif color_count == 1:
                corners += 1
            elif color_count == 2:
                if (i, j) in cells and (i-1, j-1) in cells or (i-1, j) in cells and (i, j-1) in cells:
                    corners += 2
            elif color_count == 3:
                corners += 1
            elif color_count == 4:
                pass

    return corners
                

def part2():
    data = readers.read_input("12.txt")

    visited = set()
    sum = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (i, j) in visited:
                continue
            stack = [(i, j)]
            area = 0
            cells = []
            while stack:
                x, y = stack.pop()
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                cells.append((x, y))
                
                area += 1
                for x_, y_ in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if utils.is_index_in_matrix((x_, y_), data, debug=True):

                        if data[x_][y_] == data[x][y]:
                            stack.append((x_, y_))
            wall_count = walls(cells, data)
            print(area, wall_count, area * wall_count, data[i][j])
            sum += area * walls(cells, data)

    print(sum)

part2()