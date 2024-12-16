

from base import *
import time

def part1():
    data = readers.read_input("16.txt")

    for i in range(len(data)):
        data[i] = list(data[i])

    current = None
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "S":
                current = (i, j)
                break

    goal = None
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "E":
                goal = (i, j)
                break

    velocity = (0, 1)
    stack = [(current, velocity, 0)]

    min = 99999999999999999999
    visited = {}
    while stack:
        # print(len(stack))
        # print(stack)
        current, velocity, point = stack.pop(0)
        # print(current, velocity, point)
        x, y = current
        
        if (x, y) in visited:
            if visited[((x, y), velocity)] <= point:
                continue
        visited[((x, y), velocity)] = point

        if current == goal:
            if point < min:
                min = point
                print(point)

        
        res = utils.run_function_on_neighbors(data, x, y, lambda x_, y_: ((x_, y_), (x_ - x, y_ - y), 1 if (x_ - x, y_ - y) == velocity else 1001 ) if data[x_][y_] != "#" and (x - x_, y - y_) != velocity else None) 

        for r in res:
            if r is None:
                continue
            current_, velocity_, point_ = r
            if (current_, velocity_) in visited and visited[(current_, velocity_)] <= point + point_:
                continue
            stack.append((current_, velocity_, point + point_))

part1()



def part2():
    data = readers.read_input("16.txt")

    for i in range(len(data)):
        data[i] = list(data[i])

    current = None
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "S":
                current = (i, j)
                break

    goal = None
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "E":
                goal = (i, j)
                break

    velocity = (0, 1)
    stack = [(current, velocity, 0, [current])]
    min = 99999999999999999999
    visited = {}
    best_tiles = set()
    while stack:
        # print(len(stack))
        # print(stack)
        current, velocity, point, path = stack.pop(0)
        # print(current, velocity, point)
        x, y = current
        
        if (x, y) in visited:
            if visited[((x, y), velocity)] <= point:
                continue
        visited[((x, y), velocity)] = point

        if current == goal:
            if point < min:
                min = point
                best_tiles = set(path)
            elif point == min:
                best_tiles = best_tiles.union(set(path))

        
        res = utils.run_function_on_neighbors(data, x, y, lambda x_, y_: ((x_, y_), (x_ - x, y_ - y), 1 if (x_ - x, y_ - y) == velocity else 1001 ) if data[x_][y_] != "#" and (x - x_, y - y_) != velocity else None) 

        for r in res:
            if r is None:
                continue
            current_, velocity_, point_ = r
            if (current_, velocity_) in visited and visited[(current_, velocity_)] <= point + point_:
                continue
            stack.append((current_, velocity_, point + point_, path + [current_]))

    print(len(best_tiles))

part2()