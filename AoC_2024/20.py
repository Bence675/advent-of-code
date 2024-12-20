
from base import *
import numpy as np
import math

LIMIT = 100

def get_race_track(data):
    race_track = np.zeros((len(data), len(data[0])), dtype=int)
    start = [(y, x) for y in range(len(data)) for x in range(len(data[0])) if data[y][x] == "S"][0]
    end = [(y, x) for y in range(len(data)) for x in range(len(data[0])) if data[y][x] == "E"][0]

    current = start
    counter = 1
    while True:
        y, x = current
        race_track[y, x] = counter
        if current == end:
            break

        neighbors = utils.run_function_on_neighbors(data, y, x, lambda y, x: (y, x))
        for neighbor in neighbors:
            y_, x_ = neighbor
            if race_track[y_, x_] == 0 and data[y_][x_] != "#":
                current = neighbor
                break
        counter += 1
    
    return race_track

def part1():
    data = readers.read_input("20.txt")

    race_track = get_race_track(data)

    print(race_track)

    res = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            neighbors = utils.run_function_on_neighbors(race_track, y, x, lambda a: a)
            neighbors = [neighbor for neighbor in neighbors if neighbor != 0]

            if len(neighbors) < 2:
                continue
            max_diff = max(neighbors) - min(neighbors) - 2
            if max_diff == 0:
                continue
            if max_diff in res:
                res[max_diff].append((y, x))
            else:
                res[max_diff] = [(y, x)]

    counter = 0
    for key in res:
        if key >= 100:
            counter += len(res[key])

    print(counter)

# part1()

def part2():
    data = readers.read_input("20.txt")
    race_track = get_race_track(data)


    res = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            for i in range(-20, 21):
                for j in range(-20, 21):
                    if abs(i) + abs(j) > 20:
                        continue
                    if y + i < 0 or y + i >= len(data) or x + j < 0 or x + j >= len(data[0]) or data[y][x] == "#" or data[y + i][x + j] == "#":
                        continue

                    distance = race_track[y + i, x + j] - race_track[y, x] - abs(i) - abs(j)
                    if distance >= LIMIT:
                        if distance in res:
                            res[distance].append((y, x, y + i, x + j))
                        else:
                            res[distance] = [(y, x, y + i, x + j)]

    counter = 0
    for key in res:
        counter += len(res[key])
    print(counter)
                        
part2()
