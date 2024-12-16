
from base import *

def push_box(map_tiles, current, direction):
    if map_tiles[current[0] + direction[0]][current[1] + direction[1]] == "#":
        return map_tiles, False
    if map_tiles[current[0] + direction[0]][current[1] + direction[1]] == "O":
        map_tiles, success = push_box(map_tiles, (current[0] + direction[0], current[1] + direction[1]), direction)
        if not success:
            return map_tiles, False
    map_tiles[current[0] + direction[0]][current[1] + direction[1]] = "O"
    map_tiles[current[0]][current[1]] = "."

    return map_tiles, True

def part1():
    data = readers.read_input("15.txt")
    map_tiles = []
    i = 0
    while True:
        if data[i] == "":
            i += 1
            break
        map_tiles.append([x for x in data[i]])
        i += 1

    moves = ''.join(data[i:])

    current = None
    for i in range(len(map_tiles)):
        for j in range(len(map_tiles[i])):
            if map_tiles[i][j] == "@":
                current = (i, j)
                break

    for m in moves:
        direction = None
        if m == "^":
            direction = (-1, 0)
        elif m == "v":
            direction = (1, 0)
        elif m == "<":
            direction = (0, -1)
        elif m == ">":
            direction = (0, 1)
        else:
            raise Exception("Invalid move")
        
        if map_tiles[current[0] + direction[0]][current[1] + direction[1]] == "#":
            continue
        if map_tiles[current[0] + direction[0]][current[1] + direction[1]] == "O":
            map_tiles, success = push_box(map_tiles, (current[0] + direction[0], current[1] + direction[1]), direction)
            if not success:
                continue
        map_tiles[current[0] + direction[0]][current[1] + direction[1]] = "@"
        map_tiles[current[0]][current[1]] = "."
        current = (current[0] + direction[0], current[1] + direction[1])

    s = 0
    for i in range(len(map_tiles)):
        for j in range(len(map_tiles[i])):
            if map_tiles[i][j] == "O":
                s += 100 * i + j

    print(s)
     
part1()

"""
def push_box2(map_tiles, current, direction):
    #print(map_tiles)
    map_tiles_copy = [x.copy() for x in map_tiles]
    if map_tiles[current[0] + direction[0]][current[1] + direction[1]] == "#":
        return map_tiles, False
    if map_tiles[current[0] + direction[0]][current[1] + direction[1]] == "[":
        map_tiles, success =  push_box2(map_tiles, (current[0] + direction[0], current[1] + direction[1]), direction)
        if not success:
            return map_tiles_copy, False
        if direction[0] != 0:
            map_tiles, success = push_box2(map_tiles, (current[0] + direction[0], current[1] + direction[1] + 1), direction)
            if not success:
                return map_tiles_copy, False
            
        if direction[0] != 0:
            map_tiles[current[0] + direction[0]][current[1] + direction[1]] = "["
            map_tiles[current[0] + direction[0]][current[1] + direction[1] + 1] = "]"
        else:
            if direction[1] == 1:
                map_tiles[current[0] + direction[0]][current[1] + direction[1]] = "["
                map_tiles[current[0] + direction[0]][current[1] + direction[1] + 1] = "]"
            else:
                map_tiles[current[0] + direction[0]][current[1] + direction[1] - 1] = "["
                map_tiles[current[0] + direction[0]][current[1] + direction[1]] = "]"

    if map_tiles[current[0] + direction[0]][current[1] + direction[1]] == "]":
        map_tiles, success =  push_box2(map_tiles, (current[0] + direction[0], current[1] + 2 * direction[1]), direction)
        if not success:
            return map_tiles_copy, False
        if direction[0] != 0:
            map_tiles, success = push_box2(map_tiles, (current[0] + direction[0], current[1] + direction[1] - 1), direction)
            if not success:
                return map_tiles_copy, False
        
        if direction[0] != 0:
            map_tiles[current[0] + direction[0]][current[1] + direction[1]] = "["
            map_tiles[current[0] + direction[0]][current[1] + direction[1] + 1] = "]"
        else:
            if direction[1] == 1:
                map_tiles[current[0] + direction[0]][current[1] + direction[1]] = "["
                map_tiles[current[0] + direction[0]][current[1] + direction[1] + 1] = "]"
            else:
                map_tiles[current[0] + direction[0]][current[1] + direction[1] - 1] = "["
                map_tiles[current[0] + direction[0]][current[1] + direction[1]] = "]"
    print("Hiiiiii hiiiii")
    map_tiles[current[0]][current[1]] = "."

    return map_tiles, True
"""

def vertical_push(map_tiles, current, direction):
    map_copy = [x.copy() for x in map_tiles]
    if map_tiles[current[0] + direction][current[1]] == "#":
        return map_tiles, False
    
    if map_tiles[current[0] + direction][current[1]] == "[":
        map_tiles, success = vertical_push(map_tiles, (current[0] + direction, current[1]), direction)
        if not success:
            return map_tiles, False
        map_tiles, success = vertical_push(map_tiles, (current[0] + direction, current[1] + 1), direction)
        if not success:
            return map_copy, False
        map_tiles[current[0] + 2 * direction][current[1]] = "["
        map_tiles[current[0] + 2 * direction][current[1] + 1] = "]"
        map_tiles[current[0] + direction][current[1]] = "."
        map_tiles[current[0] + direction][current[1] + 1] = "."
    if map_tiles[current[0] + direction][current[1]] == "]":
        map_tiles, success = vertical_push(map_tiles, (current[0] + direction, current[1]), direction)
        if not success:
            return map_tiles, False
        map_tiles, success = vertical_push(map_tiles, (current[0] + direction, current[1] - 1), direction)
        if not success:
            return map_copy, False
        map_tiles[current[0] + 2 * direction][current[1] - 1] = "["
        map_tiles[current[0] + 2 * direction][current[1]] = "]"
        map_tiles[current[0] + direction][current[1]] = "."
        map_tiles[current[0] + direction][current[1] - 1] = "."
    return map_tiles, True

def horizontal_push(map_tiles, current, direction):
    if direction == 1:
        if map_tiles[current[0]][current[1] + 3] == "#":
            return map_tiles, False
        if map_tiles[current[0]][current[1] + 3] == "[":
            map_tiles, success = horizontal_push(map_tiles, (current[0], current[1] + 2), direction)
            if not success:
                return map_tiles, False
        if map_tiles[current[0]][current[1] + 1] == "]":
            raise Exception("Invalid map")
        map_tiles[current[0]][current[1] + 2] = "["
        map_tiles[current[0]][current[1] + 3] = "]"
        map_tiles[current[0]][current[1] + 1] = "."
        
    else:
        if map_tiles[current[0]][current[1] - 3] == "#":
            return map_tiles, False
        if map_tiles[current[0]][current[1] - 3] == "]":
            map_tiles, success = horizontal_push(map_tiles, (current[0], current[1] - 2), direction)
            if not success:
                return map_tiles, False
        if map_tiles[current[0]][current[1] - 1] == "[":
            raise Exception("Invalid map")
        map_tiles[current[0]][current[1] - 3] = "["
        map_tiles[current[0]][current[1] - 2] = "]"
        map_tiles[current[0]][current[1] - 1] = "."

    return map_tiles, True
            

def part2():
    data = readers.read_input("15.txt")

    for i in range(len(data)):
        data[i] = data[i].replace("#", "##")
        data[i] = data[i].replace("O", "[]")
        data[i] = data[i].replace(".", "..")
        data[i] = data[i].replace("@", "@.")
        

    map_tiles = []
    i = 0
    while True:
        if data[i] == "":
            i += 1
            break
        map_tiles.append([x for x in data[i]])
        i += 1

    moves = ''.join(data[i:])


    current = None
    for i in range(len(map_tiles)):
        for j in range(len(map_tiles[i])):
            if map_tiles[i][j] == "@":
                current = (i, j)
                break


    for m in moves:
        direction = None
        if m == "^":
            direction = (-1, 0)
        elif m == "v":
            direction = (1, 0)
        elif m == "<":
            direction = (0, -1)
        elif m == ">":
            direction = (0, 1)
        else:
            raise Exception("Invalid move")
        
        if map_tiles[current[0] + direction[0]][current[1] + direction[1]] == "#":
            continue
        if map_tiles[current[0] + direction[0]][current[1] + direction[1]] == "[" or map_tiles[current[0] + direction[0]][current[1] + direction[1]] == "]":
            if direction[0] == 0:
                map_tiles, success = horizontal_push(map_tiles, current, direction[1])
                if not success:
                    continue
            else:
                map_tiles, success = vertical_push(map_tiles, current, direction[0])
                if not success:
                    continue

        map_tiles[current[0] + direction[0]][current[1] + direction[1]] = "@"
        map_tiles[current[0]][current[1]] = "."
        current = (current[0] + direction[0], current[1] + direction[1])
        

    s = 0
    for i in range(len(map_tiles)):
        for j in range(len(map_tiles[i])):
            if map_tiles[i][j] == "[":
                s += 100 * i + j


    print(s)

part2()