
import numpy as np

def read_input():
    file = open("8.txt", "r")
    lines = []
    while True:
        line = file.readline()[:-1]
        if not line:
            break
        lines.append(line)

    groups = {}
    for i in range(0, len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != '.':
                if lines[i][j] in groups:
                    groups[lines[i][j]].append(np.array((i, j)))
                else:
                    groups[lines[i][j]] = [np.array((i, j))]

    return lines, groups

def part1():
    lines, groups = read_input()
    
    H, W = len(lines), len(lines[0])

    antinodes = set()

    counter = 0
    for key in groups:
        for i in range(len(groups[key])):
            for j in range(i+1, len(groups[key])):
                diff = groups[key][i] - groups[key][j]
                antinode1 = groups[key][i] + diff 
                antinode2 = groups[key][j] - diff
                if antinode1[0] >= 0 and antinode1[0] < H and antinode1[1] >= 0 and antinode1[1] < W: # and lines[antinode1[0]][antinode1[1]] == '.':
                    antinodes.add((int(antinode1[0]), int(antinode1[1])))
                    print(key, groups[key][i], groups[key][j], antinode1)
                if antinode2[0] >= 0 and antinode2[0] < H and antinode2[1] >= 0 and antinode2[1] < W: # and lines[antinode2[0]][antinode2[1]] == '.':
                    antinodes.add((int(antinode2[0]), int(antinode2[1])))
                    print(key, groups[key][i], groups[key][j], antinode2)

    print(len(antinodes))
    print(antinodes)

def part2():
    lines, groups = read_input()
    
    H, W = len(lines), len(lines[0])

    antinodes = set()

    counter = 0
    for key in groups:
        for i in range(len(groups[key])):
            for j in range(i+1, len(groups[key])):
                diff = groups[key][i] - groups[key][j]
                antinode = groups[key][i]
                antinodes.add((int(antinode[0]), int(antinode[1])))
                while True:
                    antinode = antinode + diff
                    if antinode[0] >= 0 and antinode[0] < H and antinode[1] >= 0 and antinode[1] < W:
                        antinodes.add((int(antinode[0]), int(antinode[1])))
                        print(key, groups[key][i], groups[key][j], antinode)
                    else:
                        break
                antinode = groups[key][j]
                antinodes.add((int(antinode[0]), int(antinode[1])))
                while True:
                    antinode = antinode - diff
                    if antinode[0] >= 0 and antinode[0] < H and antinode[1] >= 0 and antinode[1] < W: # and lines[antinode2[0]][antinode2[1]] == '.':
                        antinodes.add((int(antinode[0]), int(antinode[1])))
                        print(key, groups[key][i], groups[key][j], antinode)
                    else:
                        break

    print(len(antinodes))
    print(antinodes)

                

    

part2()