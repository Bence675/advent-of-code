
from base import *

def part1():
    data = readers.read_input("3.txt")
    x, y = 0, 0
    visited = set()
    visited.add((x, y))
    for i in range(len(data)):
        if data[i] == "^":
            y += 1
        elif data[i] == "v":
            y -= 1
        elif data[i] == ">":
            x += 1
        elif data[i] == "<":
            x -= 1
        visited.add((x, y))
    print(len(visited))

part1()

def part2():
    data = readers.read_input("3.txt")
    x1, y1 = 0, 0
    x2, y2 = 0, 0

    visited = set()
    visited.add((x1, y1))

    for i in range(len(data)):
        if i % 2 == 0:
            if data[i] == "^":
                y1 += 1
            elif data[i] == "v":
                y1 -= 1
            elif data[i] == ">":
                x1 += 1
            elif data[i] == "<":
                x1 -= 1
            visited.add((x1, y1))
        else:
            if data[i] == "^":
                y2 += 1
            elif data[i] == "v":
                y2 -= 1
            elif data[i] == ">":
                x2 += 1
            elif data[i] == "<":
                x2 -= 1
            visited.add((x2, y2))

    print(len(visited))

part2()