
from base import *
from tqdm import tqdm
import numpy as np

def is_possible_design(towels, design):
    if len(design) == 0:
        return True
    for towel in towels:
        if len(towel) > len(design):
            continue
        # print(towel, design)
        # print(towel, design[:len(towel)])
        # print(len(towel), len(design[:len(towel)]))
        # print(towel == design[:len(towel)])
        if towel == design[:len(towel)]:
            success = is_possible_design(towels, design[len(towel):])
            if success:
                return True
        
    return False
            

def part1():
    data = readers.read_input("19.txt", sep=", ")
    towels = data[0]
    towels = [towel.replace("\n", "") for towel in towels]
    designs = data[2:]
    designs = [design.replace("\n", "") for design in designs]

    count = 0
    for design in designs:
        if is_possible_design(towels, design):
            count += 1

    print(count)

part1()
print("-------------")

def possible_design_count2(towels, design, starts = None, ends = None):   
    starts = np.zeros((len(towels), len(design)), dtype=int)
    ends = np.zeros((len(towels), len(design)), dtype=int)
    for i, towel in enumerate(towels):
        for j in range(len(design)):
            if design[j:].startswith(towel):
                starts[i, j] = 1
            if design[:j + 1].endswith(towel):
                ends[i, j] = 1
                
    for i in range(1, len(design)):
        ended = [j for j in range(len(towels)) if ends[j, i-1] == 1 and starts[j, i - len(towels[j])] != 0]
        for j in range(len(towels)):
            if starts[j, i] != 0:
                starts[j, i] = sum([starts[k, i-len(towels[k])] for k in ended])
        
    return sum([starts[i, len(design) - len(towels[i])] for i in range(len(towels))])

        
        
            

def part2():
    data = readers.read_input("19.txt", sep=", ")
    towels = data[0]
    towels = [towel.replace("\n", "") for towel in towels]
    designs = data[2:]
    designs = [design.replace("\n", "") for design in designs]

    counter = 0
    for design in designs:
        count = possible_design_count2(towels, design)
        print(count)
        counter += count

    print(counter)

part2()