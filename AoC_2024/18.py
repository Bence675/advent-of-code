
from base import *
import numpy as np

NUMBER_OF_FALLING_CELLS = 1024
SIZE = 71

def part1():
    data = readers.read_input("18.txt", sep=",", transform=int)
    matrix = np.zeros((SIZE, SIZE), dtype=int)
    for i in range(NUMBER_OF_FALLING_CELLS):
        x, y = data[i]
        matrix[y][x] = 1

    stack = [((0, 0), 0)]
    visited = {}
    while stack:
        (x, y), time = stack.pop(0)
        if y == SIZE - 1 and x == SIZE - 1:
            print(time)
            break
        if matrix[x][y] == 1:
            continue
            
        if (x, y) in visited:
            if visited[(x, y)] <= time:
                continue
            visited[(x, y)] = time

        new_coords = utils.run_function_on_neighbors(matrix, x, y, lambda x, y: (x, y))
        for x_, y_ in new_coords:
            if ((x_, y_), time + 1) not in stack:
                if (x_, y_) not in visited or visited[(x_, y_)] > time + 1:
                    stack.append(((x_, y_), time + 1))
            
# part1()

def flood_fill(matrix, x, y):
    stack = [(x, y)]
    visited = set()
    while stack:
        x, y = stack.pop()
        if matrix[x][y] == 1:
            continue
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for x_, y_ in utils.run_function_on_neighbors(matrix, x, y, lambda x, y: (x, y)):
            if (x_, y_) not in visited:
                stack.append((x_, y_))
    return visited

def part2():
    data = readers.read_input("18.txt", sep=",", transform=int)
    matrix = np.zeros((SIZE, SIZE), dtype=int)
    
    start = 0
    end = len(data) - 1

    while True:
        matrix = np.zeros((SIZE, SIZE), dtype=int)
        current = (start + end) // 2
        print(current)
        for i in range(current + 1):
            x, y = data[i]
            matrix[y][x] = 1

        visited = flood_fill(matrix, 0, 0)
        print(visited)
        if (SIZE - 1, SIZE - 1) in visited:
            start = current + 1
        else:
            end = current


        if start == end:
            print(start)
            print(data[start])
            for i in range(len(matrix)):
                print(''.join(['.' if x == 0 else '#' for x in matrix[i]]))
            break
part2()