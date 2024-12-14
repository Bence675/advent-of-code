
from base import *

def read_input():
    file = open("10.txt", "r")
    res = []
    while True:
        line = file.readline()[:-1]
        if not line:
            break

        res.append([int(x) for x in line])
    return res

def trailhead_count(data, i, j, visited_only_once = True):
    visited = set()
    stack = [(i, j)]
    res = 0
    while stack:
        x, y = stack.pop()
        if visited_only_once and (x, y) in visited:
            continue
        visited.add((x, y))
        if data[x][y] == 9:
            res += 1

            continue

        for x_, y_ in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if utils.is_index_in_matrix((x_, y_), data) and data[x_][y_] - 1 == data[x][y]:
                stack.append((x_, y_))

    return res


        

def part1():
    data = read_input()
    sum = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 0:
                sum += trailhead_count(data, i, j)

    print(sum)

def part2():
    data = read_input()
    sum = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 0:
                sum += trailhead_count(data, i, j, visited_only_once=False)

    print(sum)

part1()

part2()