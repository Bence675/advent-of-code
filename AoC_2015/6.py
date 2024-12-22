
from base import *
import numpy as np

def part1():
    data = readers.read_input("6.txt")

    lights = np.zeros((1000, 1000), dtype=int)

    for line in data:
        if line[0] == "toggle":
            start = line[1].split(",")
            end = line[3].split(",")
            start = (int(start[0]), int(start[1]))
            end = (int(end[0]), int(end[1]))
            for y in range(start[0], end[0] + 1):
                for x in range(start[1], end[1] + 1):
                    lights[y, x] = 1 - lights[y, x]

        elif line[0] == "turn":
            start = line[2].split(",")
            end = line[4].split(",")
            start = (int(start[0]), int(start[1]))
            end = (int(end[0]), int(end[1]))
            if line[1] == "on":
                for y in range(start[0], end[0] + 1):
                    for x in range(start[1], end[1] + 1):
                        lights[y, x] = 1
            elif line[1] == "off":
                for y in range(start[0], end[0] + 1):
                    for x in range(start[1], end[1] + 1):
                        lights[y, x] = 0
            else:
                raise ValueError("Invalid input")
        
    print(np.sum(lights))

part1()

def part2():
    data = readers.read_input("6.txt")

    lights = np.zeros((1000, 1000), dtype=int)

    for line in data:
        if line[0] == "toggle":
            start = line[1].split(",")
            end = line[3].split(",")
            start = (int(start[0]), int(start[1]))
            end = (int(end[0]), int(end[1]))
            for y in range(start[0], end[0] + 1):
                for x in range(start[1], end[1] + 1):
                    lights[y, x] += 2

        elif line[0] == "turn":
            start = line[2].split(",")
            end = line[4].split(",")
            start = (int(start[0]), int(start[1]))
            end = (int(end[0]), int(end[1]))
            if line[1] == "on":
                for y in range(start[0], end[0] + 1):
                    for x in range(start[1], end[1] + 1):
                        lights[y, x] += 1
            elif line[1] == "off":
                for y in range(start[0], end[0] + 1):
                    for x in range(start[1], end[1] + 1):
                        if lights[y, x] > 0:
                            lights[y, x] -= 1
            else:
                raise ValueError("Invalid input")
        
    print(np.sum(lights))

part2()